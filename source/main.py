import corteza_instance
import corteza_last_record
import corteza_stations
import noaa_records
import datetime

def post_records(station_records, each):
    try:
        for day in station_records.json:
            data = '{"values":' \
                        '[{"name":"Station","value":"'+ each['station'] +'"},' \
                        '{"name":"Date","value":"' + day['DATE'] + '"},' \
                        '{"name":"Temp_Max","value":"'+ (day['TMAX'] if "TMAX" in day else '') +'"},' \
                        '{"name":"Temp_Min","value":"'+ (day['TMIN'] if "TMIN" in day else '') +'"},' \
                        '{"name":"Temp_Avg","value":"'+ (day['TAVG'] if "TAVG" in day else '') +'"},' \
                        '{"name":"Precip_Liquid","value":"'+ (day['PRCP'] if "PRCP" in day else '') +'"},' \
                        '{"name":"Precip_Snow","value":"'+ (day['SNOW'] if "SNOW" in day else '') +'"}' \
                    ']}'
            request = corteza_inst.session.post('https://corteza.keithkorman.com/api/compose/namespace/370633750091923458/module/370634812425240578/record/', headers=headers, data=data)
    except:
        pass

corteza_inst = corteza_instance.instance()

stations = corteza_stations.stations(corteza_inst).list

headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}

end_date = datetime.date.today() + datetime.timedelta(days=-7)

try:
    for each in stations:
        station_last_record = corteza_last_record.last_record(corteza_inst, each['station'])
        if station_last_record.date == None:
            year = 1900
            while year < (end_date.year - 10):
                try:
                    station_records = noaa_records.records(each['station_id'], datetime.date(year,1,1).strftime('%Y-%m-%d'), datetime.date(year+9,12,31).strftime('%Y-%m-%d'))
                    # post_records(station_records, each)
                except:
                    pass
                year += 10
            station_records = noaa_records.records(each['station_id'], datetime.date(year,1,1).strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            # post_records(station_records, each)            
        else:
            start_date = station_last_record.date + datetime.timedelta(days=1)
            if end_date >= start_date:
                station_records = noaa_records.records(each['station_id'], start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
                post_records(station_records, each)
except:
    pass