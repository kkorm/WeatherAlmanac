from weather_api import monthly_record

class almanac_table:
    def __init__(self, office, station, year, month):
        pass

    def __get_month(self, office, station, year, month):
        record = record(office, station, year, month)
        return record.get_month()

    def get_string():
