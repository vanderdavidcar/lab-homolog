from netmiko import ConnectHandler
from getpass import getpass
import net_conn
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
import os

start_time = datetime.now()
# username = input('Enter your SSH username: ')
# password = getpass()

#with open("R1") as f:
#    devices_list = f.read().splitlines()
devices_list = ["R1"]
def send_config(devices_list):
    for devices in devices_list:
        print("#" * 78)
        iosv = net_conn.netmiko_lab(devices)
        print('Connecting to device:  ' + devices)
        net_connect = ConnectHandler(**iosv)
    
        command1 = net_connect.send_config_from_file(f'R1_bgp_community.cfg')
        print("--------------- APPLIED CONFIG ---------------\n")
        print(command1)
        #print("--------------- POST CONFIG ---------------\n")
        #command2 = net_connect.send_command("show etherchannel summary")
        #print(command2)

        end_time = datetime.now()
        print("Total time: {}".format(end_time - start_time))

send_config(devices_list)