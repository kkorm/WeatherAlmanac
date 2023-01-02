import requests
import json
import re

class offices:
    def __init__(self):
        pass

    def list(self):
        request_path = "https://api.weather.gov/offices/a" # Dummy path that provides error message with list of valid offices
        json_request = json.loads(requests.get(request_path).text)
        office_list = re.findall("[A-Z]{3}", str(json_request))
        for each in office_list:
            if re.fullmatch("[A-Z]{3}", each) == None:
                return []
        office_list.remove("NWS")
        return office_list