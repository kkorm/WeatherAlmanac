import requests
from html.parser import HTMLParser
from datetime import date

class web_record:
    def __init__(self, site, station, year, month):
        version = web_record.__calc_version(year, month)
        request_path = "https://forecast.weather.gov/product.php?site=" + str(site) + "&issuedby=" + str(station) + "&product=CF6&format=txt&version=" + str(version) + "&glossary=0"
        raw_request = requests.get(request_path)
        parsed_request = web_record.__parse(raw_request.text)       

    def get_month():
        pass

    def get_day(day):
        pass

    def __calc_version(year, month):
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

    def __parse(raw):
        content_start = "DY MAX MIN AVG DEP HDD CDD  WTR  SNW DPTH SPD SPD DIR MIN PSBL S-S WX    SPD DR\n================================================================================"
        content_end = "================================================================================"

        content_body = raw.split(content_start)[1].split(content_end)[0]
        print(content_body)
        

        


