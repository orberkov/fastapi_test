import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, wait

from src.api_services.cache_service import CacheService
from src.api_services.http_service import HttpApiService
from src.api_services.api_scraper_result import ApiScraperResult
from src.api_services.api_result import ApiResult
from src.api_services.service_base import ServiceBase
from src.api_services.service_config import ServiceConfig
from multiprocessing import Pool

from src.config_source import ConfigSource


class ApiScraper:
    config_arr: list[ServiceConfig] = []
    services: list[ServiceBase] = []
    pool: Pool

    def __init__(self, config_source: ConfigSource, cache_service: CacheService):
        self.cache_service = cache_service
        config_json = config_source.get()
        self.config_arr = self._parse_json(config_json)

    async def get_data(self, ip_address) -> ApiScraperResult:
        cached_result = self.cache_service.get(ip_address)
        if cached_result is not None:
            return cached_result
        else:
            futures: list = []
            result = ApiScraperResult()
            api_results: list[ApiResult] = []

            start = time.time()
            with ThreadPoolExecutor(2) as executor:
                for service in self.services:
                    futures.append(executor.submit(service.run, ip_address))

            wait(futures)

            for future in futures:
                api_results.append(future.result())

            end = time.time()

            await self.enrice_result(result, api_results, start, end)

            self.cache_service.set(ip_address, result)

            return result

    async def enrice_result(self, result, api_results, start, end):
        result.metrics['total'] = {"time": round(end - start, 2)}
        for api_result in api_results:
            result.raw_data[api_result.api_name] = api_result.raw
            result.metrics[api_result.api_name] = {"status": api_result.status, "time": api_result.duration_ml}

        print('****')
        print(set(map(lambda r: r.status, api_results)))
        all_known_statuses = set(map(lambda r: r.status, api_results))
        common_status = 'mixed'
        if len(all_known_statuses) == 1:
            common_status = all_known_statuses.pop()

        result.metrics['total']['status'] = common_status

    def _parse_json(self, config_json) -> list[ServiceConfig]:
        self.config_arr = []
        for config in config_json:
            print('Loading service: {}', config['name'])
            conf = ServiceConfig(
                config['name'], config['protocol'], config['host'], config['path'])
            self.config_arr.append(conf)

        for service_config in self.config_arr:
            self.services.append(HttpApiService(service_config))

        self.pool = Pool(processes=len(self.config_arr))


