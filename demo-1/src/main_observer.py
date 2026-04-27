from bluetooth import BLE
from time import sleep_ms
from machine import Pin

from aux import ScanResult


ble_scan_interval_us = 3000000
ble_scan_window_us = 2000000
observer = BLE()
observer.active(True)
observer.irq(ScanResult.handler)
observer.gap_scan(0,ble_scan_interval_us, ble_scan_window_us)


scan_result = None
led = Pin(8, Pin.OUT)
while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)