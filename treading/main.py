from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from utils.dev_conn import netmiko_connection
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException

with open("/home/chetos/projetos-git/lab-homolog/devices") as f:
    devices = f.read().splitlines()

error_data_list = []

def execute_command(devices, command):
    try: 
        print(f'{str(devices).upper()}:: Starting process ...')
        iosv = netmiko_connection(devices)
        net_connect = ConnectHandler(**iosv)
    
    except NetMikoTimeoutException as err:
        print(f"{devices} Connection timeout, try again... :: {err}")

    except NetMikoAuthenticationException as err:
        print(f"{devices} Authentication failed, please check credentials:: {err}")

    except Exception:
        print(f"{devices} An unexpected error occurred:: {err}")

    try:
        return net_connect.send_command(command)
    
    except Exception as err:
        print(f"{devices} Error occurred:: {err}")

    print(f'{str(devices).upper()}:: Connecting to device ...')        
    backupFile = open(f'/home/chetos/projetos-git/lab-homolog/treading/output/{devices}.cfg', "w+")
    backupFile.write(command)

"""
Treading to only on command
"""
with ThreadPoolExecutor(max_workers=5) as executor:
        results = [executor.submit(execute_command, device, 'show running-config') for device in devices]
        for result in results:
            print(result.result())
