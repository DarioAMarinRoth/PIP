# Docs: https://docs.micropython.org/en/latest/library/bluetooth.html
# Docs: https://docs.micropython.org/en/latest/library/network.WLAN.html

# Hay que copiar los dos archivos a la placa (este y aux). Además, este hay que copiarlo con el nombre main para que se
# ejecute solo automáticamente.
#
# Nota de Daro a Mati: si estás usando PyCharm con el plugin de MicroPython te podés hacer una Run/Debug Configuration
# para cargar los scripts directamente con Shift+F10. Si lo haces, subí los archivos originales y después le cambias
# el nombre del archivo directamente desde el file system de la placa. Lógicamente hay que reiniciarla para que te lo
# tome como main. Después reseteas la placa con Ctrl+D desde el tab de MicroPython tools y GG.

import network
from bluetooth import BLE
from machine import Pin
from time import sleep_ms

from aux import encode_name

beacon_name = "BEACON_1" # TODO: cambiar el nombre si corresponde
advertising_interval_us = 1000000
broadcaster = BLE()
broadcaster.active(True)
payload = encode_name(beacon_name)
broadcaster.gap_advertise(advertising_interval_us, adv_data=payload, connectable=False)

access_point = network.WLAN(network.AP_IF)
access_point.active(True)
access_point.config(ssid=beacon_name, max_clients=0)


led = Pin(8, Pin.OUT)
while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)