from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from net_conn import netmiko_connection
import re
with open("devices") as f:
    hosts = f.read().splitlines()


for devices in hosts:
    iosv = netmiko_connection(devices)
    print(f"Connecting:: {str(devices)}\n")
    # A variable "default_enter" has a press enter to confirm users delete
    net_connect = ConnectHandler(**iosv, default_enter="\r\n")
    
    # Show usernames on devices
    show_cmd = net_connect.send_config_from_file("banner.cfg")
    #show_cmd = net_connect.send_config_set("no banner motd")
    print(show_cmd)
