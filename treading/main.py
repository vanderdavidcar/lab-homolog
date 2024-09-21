from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from utils.dev_conn import netmiko_connection
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from datetime import datetime

start_time = datetime.now()

with open("devices") as f:
    devices = f.read().splitlines()

def execute_command(devices, command):
    try: 
        iosv = netmiko_connection(devices)
        net_connect = ConnectHandler(**iosv)
        net_connect.send_command("show version")
        print(f"{devices}:: Connection Sucessful")


    # Netmiko Handling error
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as e:
        dict_error = (dict(name=devices, error=e))
        error = str(dict_error)
        print(f"{devices}:: Connection Failed")

        # Create a error file
        with open("errors/errors.txt", 'a', encoding="utf-8") as f:
            f.write(f"{error}\n")

"""         
Treading to only on command
"""
with ThreadPoolExecutor(max_workers=2) as executor:
    results = [executor.submit(execute_command, device, 'show version') for device in devices]
#    for result in results:
#        print(result.result())

end_time = datetime.now()
print("")
print(f'Devices:: {len(devices)}')
print('Duration:: {}'.format(end_time - start_time))
