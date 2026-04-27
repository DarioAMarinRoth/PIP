from network import WLAN
from time import sleep_ms

PREFIX = "BEACON"
station = WLAN(WLAN.IF_STA)
station.active(True)

while True:
    scan_result = station.scan()
    networks = [(ssid, rssi) for (ssid, bssid, channel, rssi, security, hidden) in scan_result]

    for network in networks:
        ssid = network[0].decode('utf-8')
        rssi = network[1]

        if not ssid.startswith(PREFIX):
            continue

        print(f"{ssid}: {rssi} dBm")
        
    sleep_ms(500)