from repository.model.mDevice import mDevice
from repository.model.mRelay import mRelay
from config.config import Config
import json

config = Config()
config.load()

username = 'ubnt'
password = 'ubnt'

def get_all_devices():  
    results = []

    #if (len(config.devices) == 0):
    #    print('No devices found, creating devices')
    #    mp8 = mDevice('MPower Pro 8',"192.168.1.217", username, password)
    #    mpmini = mDevice('MPower Mini',"192.168.1.215", username, password)
    #    mp8.save_password = True
    #    mpmini.save_password = True
    #    devices = config.devices
    #    devices.append(mp8)
    #    devices.append(mpmini)
    #    config.save()
        
    #    results.append(mpmini)
    #    results.append(mp8)
    #else:
    print('{0} devices loaded.'.format(len(config.devices)))

    for device in config.devices:
        print('Getting information for "{}"'.format(device.name))
        mp = mDevice(device.name, device.host, device.username, device.password)
        print (mp.print_relay_states())
        results.append(mp)
            
    return results

def get_device(host):
    matches = [dev for dev in config.devices if dev.host == host]

    if (len(matches) == 0):
        return None

    return matches[0]

def save_device(device):
    matches = [dev for dev in config.devices if dev.host == device.host]

    if (len(matches) > 0):
        idx = config.devices.index(matches[0])
        config.devices[idx] = device
    else:
        config.devices.append(device)
        
    config.save()

    return 'Device with host \'{}\' saved'.format(device.host)

def delete_device(host):
    matches = [dev for dev in config.devices if dev.host == host]

    if (len(matches) == 0):
        return 'Error: Device with host \'{}\' not found'.format(host)
    
    idx = config.devices.index(matches[0])
    config.devices.pop(idx)
    config.save()
    return 'Device with host \'{}\' removed'.format(host)
