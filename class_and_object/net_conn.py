"""
Function Netmiko Connection
"""

from netmiko import ConnectHandler
from dotenv import load_dotenv
load_dotenv()
import os
import paramiko

user_lab = os.getenv("USER_LAB")
pass_lab = os.getenv("PASS_LAB")

# Netmiko Connection (nxos, ios, iosxr)
def netmiko_connection(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': user_lab,
            'password': pass_lab,
             }
