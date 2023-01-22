import requests
from datetime import date
import re

class record:
    """
    Record containing monthly data for a particular month and location.
    
    Basic usage:
    >>> r = record(office, station, year, month)
    >>> r.load(office, station, year, month)
    >>> month = r.get_month()
    >>> day = r.get_day(day)
    >>> write_to_file(filename)
    """

    def __init__(self, office, station, year, month):
        self.load(office, station, year, month)

    def load(self, office, station, year, month):
        """
        Loads new monthly data.

        :param site: NWS Office.
        :param station: NWS Station.
        :param year: Year of interest.
        :param month: Month of interest.
        """

        try:
            office_re = re.fullmatch("[a-zA-Z]{3}", office)
            station_re = re.fullmatch("[a-zA-Z]{3}", station)
            year_re = re.fullmatch("[0-9]{4}", year)
            month_re = re.fullmatch("[0-9][0-9]?", month)
            
            version = self.__calc_version(int(year), int(month))
            if version < 0:
                raise Exception("Invalid year value")
        
            request_path = "https://forecast.weather.gov/product.php?site=" + str(office) + "&issuedby=" + str(station) + "&product=CF6&format=txt&version=" + str(version) + "&glossary=0"
            raw_request = requests.get(request_path)
            self.parsed_request = self.__parse(raw_request.text) 
        except:
            self.parsed_request = ["invalid input"]
        

    def get_month(self):
        """Returns list with monthly data."""

        return self.parsed_request

    def get_day(self, day):
        """Returns list with daily data."""

        if 1 <= day <= (len(self.parsed_request) - 1):
            return self.parsed_request[day]
        return []

    def write_to_file(self, name):
        """
        Writes monthly data to a file.

        :param name: Filename.
        """
        with open(name, 'w') as file:
            for each in self.parsed_request:
                file.write(str(each) + '\n')

    def __calc_version(self, year, month):
        today = date.today()
        year_month_prod_today = today.year * 12 + today.month
        year_month_prod_request = year * 12 + month

        version = year_month_prod_today - year_month_prod_request + 1

        if version <= 0:
            return -1
        elif version > 50:
            return -2
        else:
            return version

    def __parse(self, raw):
        reg_section = "==+"
        reg_spaces = " +"
        reg_EOL = "\n"
        reg_macro = list()

        reg_macro.append(re.split(reg_section, raw)[2].lstrip())
        body_macro = re.split(reg_EOL, reg_macro[0])

        ret_list = list()
        ret_list.append(["Day", "Max Temp", "Min Temp", "Avg Temp", "Temp Dep", "Temp HDD", "Temp CDD", "Precip Watr Eq", "Precip Snow", "Precip Snow Depth", "Wind Avg", 
        "Wind Max", "Wind Dir", "Wind Min", "PSBL", "S-S", "WX", "SPD", "DR"])

        for count in range (0, len(body_macro)):
            body_macro[count] = re.sub('\s{8}', '  --  ', body_macro[count])
            ret_list.append(re.split(reg_spaces, body_macro[count]))

        for row in ret_list:
            for each in range (0, row.count("")):
                row.remove("")
            
        for each in range (0, ret_list.count([])):
            ret_list.remove([])

        return ret_list        