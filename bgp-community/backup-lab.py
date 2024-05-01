from netmiko import ConnectHandler
import net_conn
from datetime import date
from dotenv import load_dotenv
load_dotenv()
import os

# Checks if the folder based on date exist, if not, it creates it.
if not os.path.exists(f'/home/chetos/projetos-git/lab-homolog/bgp-community/{date.today()}'):
    os.makedirs(f'/home/chetos/projetos-git/lab-homolog/bgp-community/{date.today()}')

# Current time and formats it to the North American time of Month, Day, and Year.
now = date.today()

with open ('lab') as f:
    	lines =f.read().splitlines()
print (lines)

for ip in lines:
    # device_type cisco_xr works from many softwares as IOS, IOS-XR, NXOS, DellOS10
    iosxr = net_conn.netmiko_lab(ip)
    print (f"Connecting to {str(ip)}")
    
    net_connect = ConnectHandler(**iosxr)
    output = net_connect.send_command("show running")
    print(output)

    # Store backup files on specific folder created by "date.today()"
    backupFile = open(f"/home/chetos/projetos-git/lab-homolog/bgp-community/{date.today()}/{ip}.cfg", "w+")
    backupFile.write(output)
