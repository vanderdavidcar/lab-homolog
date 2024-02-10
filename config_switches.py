from netmiko import ConnectHandler
import net_conn

#with open("devices") as f:
#    host = f.read().splitlines()
    
hosts = ['s1','s2','s3','s4','s5','s6']

def config_files(hosts):
    for devices in hosts:
        print(devices)
        if devices in hosts:
            iosv = net_conn.netmiko_connection(devices)
            print(f"\n{'#'*78}\nConnecting to device model: {str(devices)}\n")
            # A variable "default_enter" has a press enter to confirm users delete
            net_connect = ConnectHandler(**iosv, default_enter="\r\n")

            # Send commands
            cmd = net_connect.send_config_from_file(f"config_{devices}_ospf.cfg")        
            print(cmd)

        
config_files(hosts)