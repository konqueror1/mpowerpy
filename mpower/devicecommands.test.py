import comm.devicecontrols as dc

c = dc.connect_to_device("192.168.1.215", "admin", "10rumncokes")

print()
    
def get_relays_status():
    print()
    print("Getting status of all relays")
    states = dc.get_device_info_json(c)
    print("Status Results:")
    print(states)
    print()
    return states

def get_single_relay_status(relay_no):
    print()
    print("Getting relay status for {}".format(relay_no))
    state = dc.get_device_info_json(c, relay_no)
    print("Status Result")
    print(state)
    print()
    return state

def get_device():
    d = dc.get_device(c)
    print(d)
    
if (__name__ == '__main__'):
    get_relays_status()
    #get_single_relay_status(1)
    get_device()

