import time
import datetime

import Adafruit_DHT

timestamp = datetime.datetime.now()

current_date = timestamp.strftime("%d" "-" "%m" "-" "%Y")
current_time = timestamp.strftime("%H" ":" "%M" ":" "%S")

sensor_name = Adafruit_DHT.DHT22
sensor_pin = 23

while 1:
    timestamp = datetime.datetime.now()
    current_time = timestamp.strftime("%H" ":" "%M" ":" "%S")
 
    humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
    temp1 = '{0:0.2f}*C'.format(temperature, humidity)
    humid1 = '{1:0.2f}%'.format(temperature, humidity)

    payload = '{ "timestamp": "' + current_time + '","temperature": ' + str(temp1) + ',"humidity": '+ str(humid1) + ' }'

    print (current_date)
    print (current_time)
    print payload
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" ")
    time.sleep(2)
