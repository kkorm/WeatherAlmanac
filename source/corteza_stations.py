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
        headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}
        request = corteza.session.get("https://corteza.keithkorman.com/api/compose/namespace/370633750091923458/module/370633907495763970/record/", headers=headers)
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