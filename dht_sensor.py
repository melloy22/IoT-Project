from machine import Pin
import dht

class DHTSensor:
    def __init__(self, pin):
        self.sensor = dht.DHT11(Pin(15))

    def read(self):
        try:
            self.sensor.measure()
            temp = self.sensor.temperature()
            hum = self.sensor.humidity()
            return temp, hum
        except OSError:
            return None, None
