from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from utils.dev_conn import netmiko_connection
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from datetime import datetime
start_time = datetime.now()

with open("devices") as f:
    devices = f.read().splitlines()

error = []
for device in devices:
    try:
        iosv = netmiko_connection(device)
        net_connect = ConnectHandler(**iosv)
    
        output = net_connect.send_command('show version', read_timeout=60)
        print(f"{device}:: Connection Successul!")
        #print(output)
    except Exception as e:
            err = (dict(name=device, erro=e))

    with open("error.cfg", "a") as f:
        f.write(f"{error.append(err)}\n")
