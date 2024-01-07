import datetime

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
        headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}
        request = corteza.session.get("https://corteza.keithkorman.com/api/compose/namespace/370633750091923458/module/370634812425240578/record/?query=Station='" + station + "'&limit=1&sort=Date+DESC", headers=headers)
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
        
