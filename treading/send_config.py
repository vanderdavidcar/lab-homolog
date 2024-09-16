from netmiko import ConnectHandler
from utils.dev_conn import netmiko_connection
from dotenv import load_dotenv
load_dotenv()


with open("/home/chetos/projetos-git/lab-homolog/devices") as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    iosv = netmiko_connection(devices)
    print(f'Connecting to device:: {devices}')
    net_connect = ConnectHandler(**iosv)
    
    command1 = net_connect.send_config_from_file(f'banner')
    print(command1)