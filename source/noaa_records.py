import requests

class records:
    """
    Class containing records for given site from NOAA
    
    Basic usage:
    >>> noaa_records = noaa_records.records(station_id, start_date, end_date)
    >>> noaa_records_json = noaa_records.json
    """

    def __init__(self, station_id, start_date, end_date):
        self.__load(station_id, start_date, end_date)

    def __load(self, station_id, start_date, end_date):
        headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}
        request = requests.get("https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&dataTypes=PRCP,SNOW,TMAX,TMIN,TAVG&stations=" + station_id + "&startDate=" + start_date + "&endDate=" + end_date + "&units=standard&format=json", headers=headers)
        self.json = request.json()