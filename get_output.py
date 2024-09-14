from netmiko import ConnectHandler
import net_conn
import threading

with open("devices") as f:
        hosts = f.read().splitlines()

#commands = ["show version","show mac address-table", "show ip arp", "show ether-channel"]
for devices in hosts:
    iosv = net_conn.netmiko_connection(devices)
    print(f"\n{'#'*78}\nConnecting to device model: {str(devices)}\n")
    # A variable "default_enter" has a press enter to confirm users delete
    net_connect = ConnectHandler(**iosv, default_enter="\r\n")
    output = net_connect.send_command("show vlan brief")
    print(output)

#def process_devices_in_parallel(hosts):
#    threads = []
#
#    for device in hosts:
#        thread = threading.Thread(target=process_devices_in_parallel, args=(device))
#        threads.append(thread)
#        thread.start()
#
#    # Wait until all the threads finish
#    for thread in threads:
#        thread.join()
#



