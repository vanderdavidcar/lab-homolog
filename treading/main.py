from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from utils.dev_conn import netmiko_connection
from utils.dev_conn import env

with open("/home/chetos/projetos-git/lab-homolog/devices") as f:
    devices = f.read().splitlines()

def execute_command(devices, command):
    
    print(f'{str(devices).upper()}:: Starting process ...')
    iosv = netmiko_connection(devices)
    net_connect = ConnectHandler(**iosv)

    output = net_connect.send_command(command)
    print(f'{str(devices).upper()}:: Connecting to device ...')    
    net_connect.disconnect()
    
    backupFile = open(f'/home/chetos/projetos-git/lab-homolog/treading/{devices}.cfg', "w+")
    backupFile.write(output)
    #return output

"""
Treading to only on command
"""
with ThreadPoolExecutor(max_workers=5) as executor:
    results = [executor.submit(execute_command, device, 'show running-config') for device in devices]
    for result in results:
        print(result.result())
