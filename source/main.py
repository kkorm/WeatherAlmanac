import corteza
import corteza_last_record
import corteza_stations
import noaa_records
import datetime

def post_records(noaa_records, each):
    for day in noaa_records.json:
        data = '{"values":' \
                    '[{"name":"Station","value":"'+ each['station'] +'"},' \
                    '{"name":"Date","value":"' + day['DATE'] + '"},' \
                    '{"name":"Temp_Max","value":"'+ (day['TMAX'] if "TMAX" in day else '') +'"},' \
                    '{"name":"Temp_Min","value":"'+ (day['TMIN'] if "TMIN" in day else '') +'"},' \
                    '{"name":"Temp_Avg","value":"'+ (day['TAVG'] if "TAVG" in day else '') +'"},' \
                    '{"name":"Precip_Liquid","value":"'+ (day['PRCP'] if "PRCP" in day else '') +'"},' \
                    '{"name":"Precip_Snow","value":"'+ (day['SNOW'] if "SNOW" in day else '') +'"}' \
                ']}'
        request = corteza.session.post('https://corteza.keithkorman.com/api/compose/namespace/370633750091923458/module/370634812425240578/record/', headers=headers, data=data)

corteza = corteza.corteza()

stations = corteza_stations.stations(corteza).list

headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}

end_date = datetime.datetime.today() + datetime.timedelta(days=-7)

for each in stations:
    station_last_record = corteza_last_record.last_record(corteza, each['station'])
    if station_last_record.date == None:
        noaa_records = noaa_records.records(each['station_id'], '1800-01-01', end_date.strftime('%Y-%m-%d'))
        # post_records(noaa_records, each)
    else:
        start_date = station_last_record.date + datetime.timedelta(days=1)
        noaa_records = noaa_records.records(each['station_id'], start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        post_records(noaa_records, each)
        