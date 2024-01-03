from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import nws_monthly_record
import corteza

corteza = corteza.corteza()

headers = {'accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}

record = nws_monthly_record.record('FGF', 'GFK', '2023', '12')
for row in record.parsed_request:
    data = '{"values":' \
                '[{"name":"Station","value":"GFK"},' \
                '{"name":"Date","value":"2023-12-' + (row[0] if int(row[0]) >= 10 else ('0' + row[0]))+ 'T12:00:00Z"},' \
                '{"name":"Temp_Max","value":"' + row[1] + '"},' \
                '{"name":"Temp_Min","value":"' + row[2] + '"},' \
                '{"name":"Temp_Avg","value":"' + row[3] + '"},' \
                '{"name":"Temp_Dep","value":"' + row[4] + '"},' \
                '{"name":"Temp_HDD","value":"' + row[5] + '"},' \
                '{"name":"Temp_CDD","value":"' + row[6] + '"},' \
                '{"name":"Precip_Liquid","value":"' + row[7] + '"},' \
                '{"name":"Precip_Snow","value":"' + row[8] + '"},' \
                '{"name":"Precip_Snow_Depth","value":"' + row[9] + '"},' \
                '{"name":"Wind_2MinSpeed_Avg","value":"' + row[10] + '"},' \
                '{"name":"Wind_2MinSpeed_Max","value":"' + row[11] + '"},' \
                '{"name":"Wind_Dir","value":"' + row[12] + '"},' \
                '{"name":"Weather_Types","value":"' + row[16] + '"},' \
                '{"name":"Wind_Peak_Speed","value":"' + row[17] + '"},' \
                '{"name":"Wind_Peak_Dir","value":"' + row[18] + '"}' \
            ']}'
    request = corteza.session.post('https://corteza.keithkorman.com/api/compose/namespace/370633750091923458/module/370634812425240578/record/', headers=headers, data=data)
    print(request.content)