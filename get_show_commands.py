from netmiko import ConnectHandler
import net_conn
import re

with open("devices") as f:
    hosts = f.read().splitlines()

def get_show_commands(hosts):
    for devices in hosts:
        iosv = net_conn.netmiko_connection(devices)
        print(f"\n{'#'*78}\nConnecting to device model: {str(devices)}\n")
        # A variable "default_enter" has a press enter to confirm users delete
        net_connect = ConnectHandler(**iosv, default_enter="\r\n")
        
        # Show usernames on devices
        show_ip = net_connect.send_command("sh ip int brief | ex una")
        show_vlan = net_connect.send_command("sh vlan brief")
        show_route = net_connect.send_command("sh ip route")

        print(show_ip,show_route,show_vlan)

get_show_commands(hosts)