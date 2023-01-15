import requests
from datetime import date
import re

class record:

    def __init__(self, site, station, year, month):
        self.load(site, station, year, month)

    def load(self, site, station, year, month):
        version = self.__calc_version(int(year), int(month))
        request_path = "https://forecast.weather.gov/product.php?site=" + str(site) + "&issuedby=" + str(station) + "&product=CF6&format=txt&version=" + str(version) + "&glossary=0"
        raw_request = requests.get(request_path)
        self.parsed_request = self.__parse(raw_request.text) 

    def get_month(self):
        return self.parsed_request

    def get_day(self, day):
        if 1 <= day <= (len(self.parsed_request) - 1):
            return self.parsed_request[day]
        return []

    def write_to_file(self, name):
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

        #reg_macro.append(re.split(reg_section, raw)[1].lstrip())
        reg_macro.append(re.split(reg_section, raw)[2].lstrip())

        #header_macro = re.split(reg_EOL, reg_macro[0])
        #body_macro = re.split(reg_EOL, reg_macro[1])
        body_macro = re.split(reg_EOL, reg_macro[0])

        ret_list = list()
        # for count in range (0, len(header_macro)):
        #     ret_list.append(re.split(reg_spaces, header_macro[count]))
        ret_list.append(["Day", "Max Temp", "Min Temp", "Avg Temp", "Temp Dep", "Temp HDD", "Temp CDD", "Precip Watr Eq", "Precip Snow", "Precip Snow Depth", "Wind Avg", 
        "Wind Max", "Wind Dir", "Wind Min", "PSBL", "S-S", "WX", "SPD", "DR"])

        for count in range (0, len(body_macro)):
            ret_list.append(re.split(reg_spaces, body_macro[count]))

        for row in ret_list:
            for each in range (0, row.count("")):
                row.remove("")
            
        for each in range (0, ret_list.count([])):
            ret_list.remove([])

        return ret_list        