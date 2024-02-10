import net_conn
import netmiko
from netmiko import ConnectHandler

class CiscoDevice:

    with open('ip_list.txt', 'r') as f:
        ipadd = f.read().splitlines()

    
    def __init__(self):
        self.connection = ConnectHandler(ip="S2",
                                        username=net_conn.user_lab, 
                                        password=net_conn.pass_lab,
                                        device_type="cisco_ios")
    def printConnection(self):
        print(self.connection)
    
    def showCommand(self):
        result = self.connection.find_prompt()
        result += self.connection.send_command(f'show run')
        print(result)
    
    def configCommand(self):
        changes = ['vlan 777', 'name Lucky7s']
        output = self.connection.send_config_set(changes)
        print(output)

sa = CiscoDevice()
sa.printConnection()
#sa.configCommand()
sa.showCommand()
sa.connection.disconnect()