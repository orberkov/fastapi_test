import json

from dataclasses import dataclass


@dataclass
class ApiScraperResult:
    metrics: json
    raw_data: json

    def __init__(self):
        self.raw_data = json.loads("{}")
        self.metrics = json.loads("{}")
