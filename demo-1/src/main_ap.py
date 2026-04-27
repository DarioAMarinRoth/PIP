# Docs: https://docs.micropython.org/en/latest/library/network.WLAN.html

import network
from time import sleep_ms
from machine import Pin



beacon_w = network.WLAN(network.AP_IF)
beacon_w.active(True)
beacon_w.config(ssid="BEACON 1", max_clients=0)

led = Pin(8, Pin.OUT)
led.value(1) # por alguna razón 1 apaga el led y 0 lo prende.

while True:
    sleep_ms(500)

