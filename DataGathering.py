import requests
import iotDevice
import time

apiRequest='https://api.thingspeak.com/update?api_key=SFV5HOTQWQHZWUP4&field1='

while True:
    v,c,p=iotDevice.getSensoryFeed()
    apiRequest+=str(v)+'&field2='+str(c)+'&field3='+str(p)
    statusCode=requests.get(apiRequest)
    print(statusCode)
    time.sleep(10)


