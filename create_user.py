from netmiko import ConnectHandler
import net_conn

with open("devices") as f:
    lines = f.read().splitlines()
print(lines)

for devices in lines:
    iosv = net_conn.netmiko_connection(devices)
    print("Connecting to " + str(devices))
    net_connect = ConnectHandler(**iosv)

    config_cmd = net_connect.send_config_from_file(f"config_cmd")
    print(config_cmd)
    show_cmd = net_connect.send_command(f"sh run | in username")
    print(show_cmd)