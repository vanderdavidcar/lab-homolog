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
    print("#"*78)
    print(f"Connecting to " + str(devices))
    # A variable "default_enter" has a press enter to confirm users delete
    net_connect = ConnectHandler(**iosv, default_enter="\r\n")
    print()
    # Show usernames on devices
    show_cmd = net_connect.send_command("sh run | in username")
    
    # Regex pattern to looking for usernames
    usr_del_pattern = re.compile(r"username (?P<username>\S+)")
    urs_match = usr_del_pattern.search(show_cmd)
    usr = re.findall(usr_del_pattern, show_cmd)

    # Regex pattern to looking for username and privilege level
    users_pattern = re.compile(r"username (?P<username>\w.+) privilege (?P<prv_lvl>\d{1,2})")
    users_match = users_pattern.search(show_cmd)
    usr_priv = re.findall(users_pattern, show_cmd)

    # Variable without value
    new_users = []

    # Find users that doesn't match with variable users
    for usernames in usr:
        if usernames not in users:
            new_users.append(usernames)

    # Create a new list of users that will be removed
    new_list = new_users

    print(f"Updated users list will be removed = {new_users}\n")

    # Loop to remove users
    for i in new_list:
        print(f"-------- POST CONFIGURATION --------\n")
        print(i)
        delete_cmd = net_connect.send_config_set(f"no username {i}")
        save_cmd = net_connect.send_command(f"save config")
        save_cmd = net_connect.send_command(f"y")
        print(delete_cmd)
        print()

    # Show users after removed list
    show_cmd = net_connect.send_command(f"sh run | in username")
    print(f"-------- AFTER CONFIGURATION --------\n")
    print(f"Users and privilege level configured in devices now\n")
    print(f"{show_cmd}\n")
