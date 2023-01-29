from dataclasses import dataclass


@dataclass
class ApiResult:
    api_name: str
    duration_ml: int
    http_code: int
    raw: str

    def set_as_error(self):
        self.http_code = 0

    def status(self):
        if self.http_code in range(200, 299):
            return 'success'
        elif self.http_code in range(500, 599) or self.http_code == 0:
            return 'error'
        elif self.http_code in range(400, 499):
            return 'unauthorized'
        else:
            return 'unknown'
