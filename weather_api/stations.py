import requests
import json
import re
from weather_api.offices import offices

class stations:
    def __init__(self):
        pass

    def list(self, office_id):
        """
        Returns a list of stations for a given NWS site.
        
        :param office_id: NWS Site.
        """

        # Verify office_id is valid
        if office_id not in offices().list():
            return []
        
        request_path = "https://api.weather.gov/offices/" + office_id
        json_request = json.loads(requests.get(request_path).text)
        office_list = [x.split("/K")[1] for x in json_request["approvedObservationStations"]]
        return office_list