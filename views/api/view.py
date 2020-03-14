import repository.mfirepo as repo
import json

def get_all_devices():
    devices = repo.get_all_devices()
    print(devices)
    values = []

    for device in devices:
        values.append(device.json_encode())

    result = {"results": values}
    return json.dumps(result)