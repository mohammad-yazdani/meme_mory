import requests
import json


class Fetch:
    endpoint: str = "http://version1.api.memegenerator.net/Generators_Search"
    key: str = "demo"
    base_params: dict = {
        "key": key
    }
    in_queue: list = []

    def __init__(self, tags: list, page_index: int = 0, page_size: int = 10):
        Fetch.base_params["pageIndex"] = page_index
        Fetch.base_params["pageSize"] = page_size
        query: str = str()
        for tag in tags:
            query += tag + " "
        Fetch.base_params["q"] = query
        r = requests.get(Fetch.endpoint, params=Fetch.base_params)
        Fetch.in_queue.append(json.loads(r.content))

    @staticmethod
    def config(endpoint: str, key: str):
        Fetch.endpoint = endpoint
        Fetch.base_params["key"] = key
