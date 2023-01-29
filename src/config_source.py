import json


class ConfigSource:
    def get(self):
        return json.load(open('./services.json', 'r'))
