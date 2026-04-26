def encode_name(name):
    name_bytes = name.encode()
    return bytes([len(name_bytes) + 1, 0x09]) + name_bytes