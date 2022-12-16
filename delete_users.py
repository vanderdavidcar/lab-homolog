from netmiko import ConnectHandler
import net_conn
import re

with open("devices") as f:
    lines = f.read().splitlines()
print(lines)

# List of users must be in devices 
users = ["vanderson", "backup"]

# Netmiko devices conection
for devices in lines:
    iosv = net_conn.netmiko_connection(devices)
    print("Connecting to " + str(devices))
    # A variable "default_enter" has a press enter to confirm users delete
    net_connect = ConnectHandler(**iosv, default_enter="\r\n")

    # Show usernames on devices
    show_cmd = net_connect.send_command("sh run | in username")
    cmd_split = show_cmd.split()
    # Split only users in cmd_split find out exatly index in each 7 value
    output_users = cmd_split[1::7]
    print(output_users)

    # Variable without value
    new_users = []

    # Find users that doesn't match with variable users
    for usrs in output_users:
        if usrs not in users:
            new_users.append(usrs)

    # Create a new list of users that will be removed
    new_list = new_users

    print(f"Updated List with users that will be removed = {new_users}")

    # Loop to remove users
    for i in new_list:
        print(f"-------- POST CONFIGURATION --------")
        print(i)
        delete_cmd = net_connect.send_config_set(f"no username {i}")
        print(delete_cmd)

    # Show users after removed list
    show_cmd = net_connect.send_command(f"sh run | in username")
    print(f"-------- AFTER CONFIGURATION --------")
    print(show_cmd)
