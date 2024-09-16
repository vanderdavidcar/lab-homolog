from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from utils.dev_conn import netmiko_connection
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException

with open("/home/chetos/projetos-git/lab-homolog/devices") as f:
    devices = f.read().splitlines()


def execute_command(devices, command):
    
    print(f'{str(devices).upper()}:: Starting process ...')
    iosv = netmiko_connection(devices)
    net_connect = ConnectHandler(**iosv)
    try:
        output = net_connect.send_command(command)
    except ConnectionRefusedError as err:
        print(f"Connection Refused: {err}")
    except TimeoutError as err:
        print(f"Connection Refused: {err}")
    except Exception as err:
        print(f"Oops! {err}")

    net_connect.disconnect()

    print(f'{str(devices).upper()}:: Connecting to device ...')        
    backupFile = open(f'/home/chetos/projetos-git/lab-homolog/treading/output/{devices}.cfg', "w+")
    backupFile.write(output)
    return output

"""
Treading to only on command
"""
with ThreadPoolExecutor(max_workers=5) as executor:
        results = [executor.submit(execute_command, device, 'show running-config') for device in devices]
        for result in results:
            print(result.result())
