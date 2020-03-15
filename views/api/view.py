import repository.mfirepo as repo
from repository.model.mDevice import mDevice
import json

def get_all_devices():
    devices = repo.get_all_devices()
    print(devices)
    values = []

    for device in devices:
        values.append(device.json_encode())

    return json_results(False, values)

def get_device(host):
    device = repo.get_device(host) 

    if (device is None):
        results = json_results(True,'Device not found.  Verify the host address you are using and try again')
    else:
        results = json_results(False, device.json_encode())

    return results

def add_device(payload):
    device = mDevice(payload['name'],payload['host'],payload['username'],payload['password'], False)
    device.save_password = True
    results = repo.save_device(device)
    
    if ('Error' in results):
        return json_results(True, results)
    
    return json_results(False, results)

def delete_device(host):
    result = repo.delete_device(host)

    if ('Error' in result):
        return json_results(True, result)
    else:
        return json_results(False, result)

def json_results(is_error, values):
    if (is_error == False):
        return json.dumps(results_value(values))
    else:
        return json.dumps(error(values))
    

def results_value(values):
    return {
        "results": "success",
        "data": values
    }

def error(message):
    return {
        "results": "failed", 
        "error_reason": message
        }
