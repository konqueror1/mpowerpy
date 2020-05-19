from repository.model.mDevice import mDevice
from repository.model.mRelay import mRelay
import comm.webrequest as webrequest
import comm.telnetclient as telnetclient
import getpass
import json
import time

def connect_to_device(host, username, password):
    return webrequest.Requester(host, username, password)

def get_device_info_json(connection, relay_no=0):
    return json.loads(connection.get_general_info(relay_no))

def get_device(connection):
    return connection.get_general_info(0)
    
