import time
from concurrent.futures import ThreadPoolExecutor, wait
from typing import List

from .cache_service import CacheService
from .http_service import HttpApiService
from .api_scraper_result import ApiScraperResult
from .api_result import ApiResult
from .service_config import ServiceConfig
from src.config_source import ConfigSource


class ApiScraper:

    def __init__(self, config_source: ConfigSource, cache_service: CacheService):
        self.cache_service = cache_service
        config_json = config_source.get()
        self.services = self._initialize_services(config_json)

    async def get_data(self, ip_address) -> ApiScraperResult:
        cached_result = self.cache_service.get(ip_address)
        if cached_result:
            return cached_result
        else:
            futures: List = []
            api_results: List[ApiResult] = []

            start = time.time()
            with ThreadPoolExecutor(2) as executor:
                for service in self.services:
                    futures.append(executor.submit(service.run, ip_address))

            wait(futures)

            end = time.time()

            for future in futures:
                api_results.append(future.result())

            result = await ApiScraperResult.get_result(api_results, start, end)

            self.cache_service.set(ip_address, result)

            return result

    @staticmethod
    def _initialize_services(config_json) -> List[ServiceConfig]:
        config_arr = []
        for config in config_json:
            print('Loading service: {}', config['name'])
            conf = ServiceConfig(
                config['name'], config['protocol'], config['host'], config['path'])
            config_arr.append(conf)

        services = []
        for service_config in config_arr:
            services.append(HttpApiService(service_config))

        return services




