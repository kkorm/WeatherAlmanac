import requests
import json
import re

class offices:
    def __init__(self):
        pass

    def list(self):
        """Returns a list of NWS sites."""

        request_path = "https://api.weather.gov/offices/a" # Dummy path that provides error message with list of valid offices
        json_request = json.loads(requests.get(request_path).text)
        office_list = re.findall("[A-Z]{3}", str(json_request))
        for each in office_list:
            if re.fullmatch("[A-Z]{3}", each) == None:
                return []
        office_list.remove("NWS")
        office_list.sort()
        return office_list