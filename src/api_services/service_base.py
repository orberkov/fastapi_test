from abc import ABC, abstractmethod

import time

from .api_result import ApiResult
from .service_config import ServiceConfig


class ServiceBase(ABC):

    def __init__(self, service_config: ServiceConfig):
        self.service_config: ServiceConfig = service_config

    def run(self, ip_address: str) -> ApiResult:
        start = time.time()
        try:
            result = self._run(ip_address)
        except:
            result = ApiResult(self.service_config.name, 0, 0, '')
        end = time.time()

        result.duration_ml = round(end - start, 2)

        if not self._is_result_valid(result):
            result.set_as_error()

        return result

    @abstractmethod
    def _run(self, ip_address: str) -> ApiResult:
        raise "Not Implemented"

    @abstractmethod
    def _is_result_valid(self, api_result: ApiResult) -> ApiResult:
        raise "Not Implemented"
