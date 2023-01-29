from dataclasses import dataclass


@dataclass
class ApiResult:
    api_name: str
    duration_ml: int
    http_code: int
    status: str
    raw: str

    def __init__(self, api_name: str, http_code: int, raw: str):
        self.api_name = api_name
        self.http_code = http_code

        if self.http_code in range(200, 299):
            self.status = 'success'
        elif self.http_code in range(500, 599):
            self.status = 'error'
        elif self.http_code in range(400, 499):
            self.status = 'unauthorized'
        else:
            self.status = 'unknown'

        self.raw = raw
