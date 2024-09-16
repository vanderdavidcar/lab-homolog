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



username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
secret = os.getenv("SECRET")

def netmiko_ios(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
            'secret': secret
             }


def get_output(dev_conn, device_type, action):
    try:
        template = env.get_template(f"templates/{device_type}_{action}.j2")
        command =  template.render()

        return dev_conn.send_command(command, read_timeout=60)
    
    except Exception as e:
        if 'Pattern not detected' in str(e):
            return 'Pattern not detected'
        else:
            return str(e)