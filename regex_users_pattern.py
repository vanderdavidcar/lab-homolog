from netmiko import ConnectHandler
import net_conn
import re

with open("devices") as f:
    lines = f.read().splitlines()
print(lines)


for devices in lines:
    iosv = net_conn.netmiko_connection(devices)
    print("Connecting to " + str(devices))
    # A variable "default_enter" has a press enter to confirm users delete
    net_connect = ConnectHandler(**iosv, default_enter="\r\n")
    # Show usernames on devices
    show_cmd = net_connect.send_command("sh run | in username")
    users_pattern = re.compile(r"username (?P<username>\w.+) privilege (?P<prv_lvl>\S+)")
    users_match = users_pattern.search(show_cmd)
    list = re.findall(users_pattern, show_cmd)

    for i in list:
        print(f"Users and Priv-Level".ljust(18) + ": " + str(i))
 