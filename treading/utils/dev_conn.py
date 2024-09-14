"""
Function Netmiko Connection
"""
# General Imports
import json
from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException
from jinja2 import Environment, FileSystemLoader

# Jinja2 Enviroment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

from dotenv import load_dotenv
load_dotenv()
import os


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
