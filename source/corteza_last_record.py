import datetime
import os
from dotenv import load_dotenv

class last_record:
    """
    Class containing last record for a given site in Corteza
    
    Basic usage:
    >>> last_record = corteza_last_record.last_record(corteza, station)
    >>> last_record_json = last_record.json
    >>> last_record_date = last_record.date
    """    

    def __init__(self, corteza, station):
        self.__load(corteza, station)

    def __load(self, corteza, station):
        load_dotenv()
        corteza_base_url=os.getenv('corteza_base_url')
        corteza_namespace_id=os.getenv('corteza_namespace_id')
        corteza_noaa_module_id=os.getenv('corteza_noaa_module_id')
        headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}
        request = corteza.session.get(corteza_base_url + '/api/compose/namespace/' + corteza_namespace_id + '/module/' + corteza_noaa_module_id + "/record/?query=Station='" + station + "'&limit=1&sort=Date+DESC", headers=headers)
        self.json = request.json()

        try:
            for element in self.json['response']['set'][0]['values']:
                if element['name'] == 'Date':
                    temp = element['value']
                    temp = temp.split("T")[0]
                    temp = temp.split("-")
                    self.date = datetime.date(int(temp[0]), int(temp[1]), int(temp[2]))
                    break
        except:
            self.date = None
        
