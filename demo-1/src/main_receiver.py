from bluetooth import BLE
from machine import Pin
from network import WLAN
from time import sleep_ms

from aux import ScanResult


ble_scan_interval_us = 3000000
ble_scan_window_us = 1000000
observer = BLE()
observer.active(True)
observer.irq(ScanResult.handler)
observer.gap_scan(0,ble_scan_interval_us, ble_scan_window_us)

PREFIX = "BEACON"
station = WLAN(WLAN.IF_STA)
station.active(True)

led = Pin(8, Pin.OUT)
while True:
    scan_result = station.scan()
    networks = [(ssid, rssi) for (ssid, bssid, channel, rssi, security, hidden) in scan_result]

    for network in networks:
        ssid = network[0].decode('utf-8')
        rssi = network[1]

        if not ssid.startswith(PREFIX):
            continue
        print(f"WLAN | {ssid}: {rssi} dBm")

    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)