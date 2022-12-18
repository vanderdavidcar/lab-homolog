from netmiko import ConnectHandler
import net_conn
import re
from regex_users_pattern import user_list

with open("devices") as f:
    lines = f.read().splitlines()
print(lines)

# List of users must be in devices 
users = ["vanderson", "backup"]

# Variable without value
new_users = []

# Find users that doesn't match with variable users
for usernames in user_list:
    if usernames not in users:
        new_users.append(usernames)

# Create a new list of users that will be removed
new_list = new_users
print(f"Updated users list will be removed = {new_users}\n")
# Looping to remove undesirable users

for i in new_list:
    print(f"-------- POST CONFIGURATION --------\n")
    print(i)
    delete_cmd = net_connect.send_config_set(f"no username {i}")
    save_cmd = net_connect.send_command(f"save config")
    save_cmd = net_connect.send_command(f"y")
    print(delete_cmd)
    print()
# Show users on devices after removed list
show_cmd = net_connect.send_command(f"sh run | in username")
print(f"-------- AFTER CONFIGURATION --------\n")
print(f"Users and privilege level configured in devices now\n")
print(f"{show_cmd}\n")