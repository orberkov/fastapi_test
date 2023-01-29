import json
from .api_result import ApiResult
from .service_base import ServiceBase
import requests


class HttpApiService(ServiceBase):
    url: str = None

    def _run(self, ip_address) -> ApiResult:
        if self.url is None:
            self.url = '{protocol}://{host}{path}'.format(
                protocol=self.service_config.protocol, host=self.service_config.host, path=self.service_config.path)

        dest = self.url.replace('<ip_address>', ip_address)

        print('dest: {}', dest)

        r = requests.get(dest)

        return ApiResult(self.service_config.name, 0, r.status_code, r.content)

    def _is_result_valid(self, api_result: ApiResult) -> bool:
        try:
            json_content = json.loads(api_result.raw)
            return json_content['status'] in str(['success', 'ok']) #if the results differ further, we'll split the implementation
        except:
            return False
