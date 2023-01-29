import redis
import pickle


def _get_key(key: str):
    return "api_cache_" + key


class CacheService:
    def __init__(self):
        self.r = redis.Redis(host='redis', port=6379, db=0)

    def get(self, key: str):
        res = self.r.get(_get_key(key))
        if res:
            print("cache hit")
            return pickle.loads(res)
        print("key is empty key="+key)
        return None

    def set(self, key: str, api_scraper_result: str):
        value = pickle.dumps(api_scraper_result, protocol=pickle.HIGHEST_PROTOCOL)
        self.r.set(_get_key(key), value, ex=60 * 60)
