import json


class JsonManager:
    def __init__(self):
        pass

    @staticmethod
    def read_json(jsonpath: str):
        with open(jsonpath) as outfile:
            return json.load(outfile)

    @staticmethod
    def write_json(data: dict, json_path: str):
        with open(json_path, 'w') as file:
            json.dump(data, file)
