from pymongo import MongoClient
import datetime
import pyowm
# 날씨 정보 
db_url = db_url = 'mongodb://192.168.0.179:27017'
# owm = pyowm.OWM('5b457f895ab57ef2daac2b9e32db5319')
# mgr = owm.weather_manager()
# # 
# with MongoClient(db_url) as client:    
#     client['mydb']['weather_info'].delete_many({})    
#     mtinfo = list(client['mydb']['mountain_info'].find())
#     for info in mtinfo:
#         lat = float(info['lat'])
#         lon = float(info['lon'])
#         obj = mgr.weather_at_coords(lat,lon)
#         data = {
#                 'lat' : lat,
#                 'lon' : lon,
#                 'wind' : obj.weather.wind(),
#                 'detailed_status' : obj.weather.detailed_status,
#                 'icon_url' : obj.weather.weather_icon_url(),
#                 'temperature' : obj.weather.temperature('celsius'),
#                 'create_time': str(datetime.datetime.now())
#         }
#         client['mydb']['weather_info'].insert_one(data)
# my = geocoder.ip()
# ip = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# ip.connect(('8.8.8.8',0))

with MongoClient(db_url) as client:    
    client['mydb']['local_latlon'].delete_many({})    
    dic_latlng = {
                    '강원도':[37.570705,126.981354],
                    '경기도':[36.571424,128.722687],
                    '경상남도':[35.556809 ,129.247284],
                    '경상북도':[35.860118 ,128.563385],
                    '광주광역시':[36.348315 ,127.390594],
                    '대구광역시':[35.005253 ,127.648773],
                    '서울특별시':[37.418163 ,126.714935],
                    '울산광역시':[35.562169 ,129.281460],
                    '인천광역시':[37.437793 ,126.975861],
                    '전라남도':[36.820279 ,127.10495],
                    '전라북도':[36.650793 ,127.478485],
                    '제주특별자치도':[35.958 ,126.712189],
                    '충청남도':[35.160337 ,126.824799],
                    '충청북도':[37.885693 ,127.733917]
    }
    for local_name,lat_lon in zip(dic_latlng.keys(),dic_latlng.values()):
        data = {
            'local_name': local_name,
            'lat': lat_lon[0],
            'lon': lat_lon[1]
        }
        client['mydb']['local_latlon'].insert_one(data)
        



