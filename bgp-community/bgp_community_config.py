from jinja2 import Template
from netmiko import ConnectHandler
import csv, re
import net_conn

"""
Get router bgp process and all neighbors to create a send-community only from established session
"""

# Devices to netmiko connection
with open("lab") as f:
    hosts = f.read().splitlines()
    print(hosts)

# Function to get informations and create a bgp community script
def bgp_community():
     
     # Netmiko connection on devices
     for devices in hosts:
          print("#" * 78)
          iosv = net_conn.netmiko_lab(devices)
          print('Connecting to device:  ' + devices)
          net_connect = ConnectHandler(**iosv)

          # Get Local ASN number
          show_ip_bgp = net_connect.send_command("show ip bgp summary")
          regex_as = "BGP.router.+local.+number.(\d+)"
          pattern_as = re.findall(regex_as, show_ip_bgp)
          for ASN in pattern_as:
               print(f"Local ASN: {ASN}")

          # Retrieve IPv4 neighbors
          show_ipv4_neigh = net_connect.send_command("show ip bgp neighbor")
          regex4 = "Session:.(\S+)"
          pattern4 = re.findall(regex4,show_ipv4_neigh)

          # Retrieve IPv6 neighbors
          show_ipv6_neigh = net_connect.send_command("show bgp ipv6 neighbor")
          regex6 = "Session:.(\S+)"
          pattern6 = re.findall(regex6,show_ipv6_neigh)

          """
          Script to configure BGP Community
          """


          print(f"\nrouter bgp {ASN}")
          print(f"address-family ipv4 unicast")
          for neigh_ipv4 in pattern4:
               print(f"neighbor {neigh_ipv4} send-community")
          
          print(f"address-family ipv6 unicast")
          for neigh_ipv6 in pattern6:
               print(f"neighbor {neigh_ipv6} send-community")
          
bgp_community()
