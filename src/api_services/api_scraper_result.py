import json

from dataclasses import dataclass
from typing import Dict


@dataclass
class ApiScraperResult:
    metrics: Dict
    raw_data: Dict

    @classmethod
    async def get_result(cls, api_results, start, end) -> 'ApiScraperResult':
        metrics = {"total": {"time": round(end - start, 2)}}
        raw_data = {}

        for api_result in api_results:
            raw_data[api_result.api_name] = api_result.raw
            metrics[api_result.api_name] = {"status": api_result.status(), "time": api_result.duration_ml}

        print('****')
        print(set(map(lambda r: r.status(), api_results)))
        all_known_statuses = set(map(lambda r: r.status(), api_results))
        # print(all_known_statuses)
        common_status = "mixed"
        if len(all_known_statuses) == 1:
            common_status = all_known_statuses.pop()

        metrics["total"]["status"] = common_status

        print(metrics)
        print(raw_data)
        return cls(metrics=metrics, raw_data=raw_data)
