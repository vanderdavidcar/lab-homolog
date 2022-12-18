import re
from netmiko import ConnectHandler
import net_conn


def dev_conn():

    with open("devices") as f:
        lines = f.read().splitlines()
    print(lines)

    for devices in lines:
        iosv = net_conn.netmiko_connection(devices)
        print("Connecting to " + str(devices))
        # A variable "default_enter" has a press enter to confirm users delete
        net_connect = ConnectHandler(**iosv, default_enter="\r\n")
        # Show usernames on devices

if __name__ == "__dev_conn__": dev_conn()

def get_usernames():
    # Regex pattern to looking for usernames
    usr_del_pattern = re.compile(r"username (?P<username>\S+)")
    usr_match = usr_del_pattern.search(dev_conn())
    usr = re.findall(usr_del_pattern, dev_conn())
get_usernames()

if __name__ == "__main__": get_usernames()    

def get_user_priv():

    # Regex pattern to looking for username and privilege level
    users_pattern = re.compile(r"username (?P<username>\w.+) privilege (?P<prv_lvl>\d{1,2})")
    users_match = users_pattern.search(dev_conn())
    usr_priv = re.findall(users_pattern, dev_conn())
    print(usr_priv)

if __name__ == "__main__": get_user_priv()

def commands():
    iosv = net_conn.netmiko_connection(devices)
    show_cmd = net_conn.net_connect.send_command("sh run | in username")
    print(show_cmd)
