from weather_api.monthly_record import record
from weather_api.offices import offices
from weather_api.stations import stations
from web_interface.almanac_table import almanac_table

record = record("fgf", "gfk", 2022, 7)
print(record.get_month())
# print(record.get_month())
# print(record.get_day(1))
# record.write_to_file("gfk2207.txt")


# office_list = offices().list()
# print(office_list)
# station_list = stations().list("FGF")
# # print(station_list)

# table = almanac_table("fgf", "gfk", 2022, 7)
# print(table.get_html_string())