#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    device = {
        "device_type": "juniper_junos",
        "host": "vmx1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "my_session.txt",
    }

    net_connect = ConnectHandler(**device)
    pprint(net_connect.send_command("show interfaces", use_textfsm=True))
    net_connect.disconnect()
