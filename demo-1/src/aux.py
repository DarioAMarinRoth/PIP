from micropython import const

def encode_name(name):
    name_bytes = name.encode()
    return bytes([len(name_bytes) + 1, 0x09]) + name_bytes

def decode_name(data: bytes):
    if len(data) < 2:
        return "N/A"

    length = data[0]

    if len(data) < length + 1:
        return "N/A"

    type_byte = data[1]
    if type_byte != 0x09:
        return "N/A"

    name_bytes = data[2:length + 1]
    return bytes(name_bytes).decode()


_IRQ_SCAN_RESULT = const(5)

class ScanResult:
    _PREFIX = "BEACON"
    _RESULT : dict[str, int] = {}
    def __init__(self):
         self.result = {}

    @staticmethod
    def handler(event, data):
        if event == _IRQ_SCAN_RESULT:
            addr_types, addr, adv_type, rssi, adv_data = data
            name = decode_name(adv_data)
            for i in range (len(ScanResult._PREFIX)):
                if name[i] != ScanResult._PREFIX[i]:
                    return
            ScanResult._RESULT[name] = rssi
            ScanResult.show_results()

    @staticmethod
    def show_results():
        for key, value in ScanResult._RESULT.items():
            print(f"BLE  | {key}: {value} dBm")