from datetime import datetime

devices = {}

def update_device(ip):
    devices[ip] = datetime.now()

def get_devices():
    result = {}
    now = datetime.now()

    for ip, last_seen in devices.items():
        diff = (now - last_seen).seconds

        if diff < 15:
            result[ip] = "ONLINE"
        else:
            result[ip] = "OFFLINE"

    return result