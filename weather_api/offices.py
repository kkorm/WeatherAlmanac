import requests
import json

class offices:
    def __init__(self):
        pass

    def list(self):
        request_path = "https://api.weather.gov/offices/a" # Dummy path that provides error message with list of valid offices
        json_request = json.loads(requests.get(request_path).text)
        trimmed_string = str(json_request["parameterErrors"][1]["message"]).removeprefix("Does not have a value in the enumeration [\"").removesuffix("\"]")
        office_list = trimmed_string.split("\",\"")
        return office_list