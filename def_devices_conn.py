from netmiko import ConnectHandler
import net_conn

#with open("devices") as f:
#    lines = f.read().splitlines()
#print(lines)

cisco = ["s1", "s2", "s3"]
nxos = ["s4", "s5", "s6"]

def device_conn(ips,model):
    for devices in ips:
        iosv = net_conn.netmiko_connection(devices)
        print(f"\n{'#'*78}\nConnecting to device model: {model}: {str(devices)}\n")
        net_connect = ConnectHandler(**iosv, default_enter="\r\n")
        show_cmd = net_connect.send_command("sh run | in username")
        #print(show_cmd)
        #config_cmd = net_connect.send_config_from_file(f"config_cmd")
        #save_cmd1 = net_connect.send_command(f"save config")
        #save_cmd2 = net_connect.send_command(f"y")
        #print(config_cmd)
        #show_cmd = net_connect.send_command(f"sh run | in username")
        #print(show_cmd)

device_conn(cisco,'ios')
device_conn(nxos,'nxos')