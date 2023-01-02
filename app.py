from monthly_record import record
from weather_api.offices import offices
from weather_api.stations import stations

# record = record("fgf", "gfk", 2022, 7)
# record.write_to_file("gfk2207.txt")
# record.load("fgf", "gfk", 2022, 8)
# record.write_to_file("gfk2208.txt")
# record.load("fgf", "gfk", 2022, 9)
# record.write_to_file("gfk2209.txt")
# ##record.get_day(29)

office_list = offices().list()
print(office_list)
station_list = stations().list("FGF")
print(station_list)
