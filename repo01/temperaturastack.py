import Adafruit_DHT
import time
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
PROBE_NAME = "PI4"

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
    print("{2} - T={0:0.1f} H={1:0.1f}".format(temperature, humidity, datetime.now()))
else:
    print("Failed to retrieve data from humidity sensor")