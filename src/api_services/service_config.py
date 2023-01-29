from dataclasses import dataclass


@dataclass
class ServiceConfig:
    name: str
    protocol: str
    host: str
    path: str


