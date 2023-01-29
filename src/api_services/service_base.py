from abc import ABC, abstractmethod

import time

from src.api_services.api_result import ApiResult
from src.api_services.service_config import ServiceConfig


class ServiceBase(ABC):

    service_config: ServiceConfig

    def __init__(self, service_config: ServiceConfig):
        self.service_config = service_config

    def run(self, ip_address: str) -> ApiResult:
        start = time.time()
        try:
            result = self._run(ip_address)
        except:
            result = ApiResult(self.service_config.name, 0, '')
            result.status = 'error'
        end = time.time()

        result.duration_ml = round(end - start, 2)

        if not self._is_result_valid(result):
            result.status = 'error'

        return result

    @abstractmethod
    def _run(self, ip_address: str) -> ApiResult:
        raise "Not Implemented"

    @abstractmethod
    def _is_result_valid(self, api_result: ApiResult) -> ApiResult:
        raise "Not Implemented"
