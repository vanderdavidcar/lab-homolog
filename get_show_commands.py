from netmiko import ConnectHandler
import net_conn
from pprint import pprint

with open("devices") as f:
    hosts = f.read().splitlines()

def get_show_commands(hosts):
    for devices in hosts:
        iosv = net_conn.netmiko_connection(devices)
        print(f"\n{'#'*78}\nConnecting to device model: {str(devices)}\n")
        # A variable "default_enter" has a press enter to confirm users delete
        net_connect = ConnectHandler(**iosv, default_enter="\r\n")
        
        # Send commands
        #cmd = net_connect.send_config_from_file("config_ospf.cfg")        
        #print(cmd)

        # Show usernames on devices
        show_trunk = net_connect.send_command("clear ip ospf process")
        print(show_trunk)

        #show_ip = net_connect.send_command("sh ip int brief | ex una",use_genie=True)
        #print(show_ip)
#
        #show_vlan = net_connect.send_command("sh vlan brief",use_genie=True)
        #print(show_vlan)
#
        #show_route = net_connect.send_command("sh ip route",use_genie=True)
        #print(show_route)
#
        #show_ospf = net_connect.send_command("sh ip ospf neigh",use_genie=True)
        #print(show_ospf)
#
        #show_bgp = net_connect.send_command("sh ip bgp summ",)
        #print(show_bgp)
        ##print(show_ip,show_vlan,show_route,show_ospf)
        
        
get_show_commands(hosts)