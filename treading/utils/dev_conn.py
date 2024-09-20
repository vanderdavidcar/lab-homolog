"""
Function Netmiko Connection
"""
# General Imports
from jinja2 import Environment, FileSystemLoader

# Jinja2 Enviroment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

from dotenv import load_dotenv
load_dotenv()
import os


user_lab = os.getenv("USERNAME")
pass_lab = os.getenv("PASSWORD")

# Netmiko Connection (nxos, ios, iosxr)
def netmiko_connection(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': user_lab,
            'password': pass_lab,
            "global_delay_factor": 4,
            "fast_cli": False,
             }
