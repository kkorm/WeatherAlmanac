import os
from dotenv import load_dotenv

class stations:
    """
    Class containing last record for a given site in Corteza
    
    Basic usage:
    >>> stations = corteza_stations.stations(corteza)
    >>> stations_list = stations.list
    """

    def __init__(self, corteza):
        self.__load(corteza)

    def __load(self, corteza):
        load_dotenv()
        corteza_base_url=os.getenv('corteza_base_url')
        corteza_namespace_id=os.getenv('corteza_namespace_id')
        corteza_stations_module_id=os.getenv('corteza_stations_module_id')
        headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}
        request = corteza.session.get(corteza_base_url + '/api/compose/namespace/' + corteza_namespace_id + '/module/' + corteza_stations_module_id + '/record/', headers=headers)
        json = request.json()

        info = ('station', 'station_id', 'office')
        self.list = list()
        try:
            for station in json['response']['set']:
                temp = dict.fromkeys(info)
                for element in station['values']:
                    if element['name'] == 'Station':
                        temp['station'] = element['value']
                    elif element['name'] == 'Station_ID':
                        temp['station_id'] = element['value']
                    elif element['name'] == 'Office':
                        temp['office'] = element['value']
                self.list.append(temp)
        except:
            pass