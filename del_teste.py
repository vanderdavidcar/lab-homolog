from netmiko import ConnectHandler
import net_conn
import re
import regex_pattern

# List of users must be in devices 
users = ["vanderson", "backup"]

# Variable without value
new_users = []

print(regex_pattern.dev_conn)

# Find users that doesn't match with variable users
for usernames in regex_pattern.get_usernames():
    if usernames not in users:
        new_users.append(usernames)

    # Create a new list of users that will be removed
    new_list = new_users
    print(f"Updated users list will be removed = {new_users}\n")

    # Looping to remove undesirable users
    for i in new_list:
        print(f"-------- POST CONFIGURATION --------\n")
        print(i)
        delete_cmd = regex_pattern.dev_conn.net_connect.send_config_set(f"no username {i}")
        save_cmd = regex_pattern.dev_conn.net_connect.send_command(f"save config")
        save_cmd = regex_pattern.dev_conn.net_connect.send_command(f"y")
        print(delete_cmd)
        print()

    # Show users on devices after removed list
    show_cmd = regex_pattern.dev_conn.net_connect.send_command(f"sh run | in username")
    print(f"-------- AFTER CONFIGURATION --------\n")
    print(f"Users and privilege level configured in devices now\n")
    print(f"{show_cmd}\n")