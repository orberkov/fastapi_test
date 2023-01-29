from dataclasses import dataclass


@dataclass
class ServiceConfig:
    name: str
    protocol: str
    host: str
    path: str

    def __init__(self, name: str, protocol: str, host: str, path: str):
        self.name = name
        self.protocol = protocol
        self.host = host
        self.path = path

