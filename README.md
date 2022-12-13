# LAB environment EVE-NG

This is my LAB environment using EVE-NG to testing my codes there are six switches and four routers

## Dependencies: Install the requirements to have all dependencies used on this project
$ pip install -r requirements

## .env
To protect credentials leaking, create a .env file with variables that will be used to connect on devices (USER_LAB/PASS_LAB).

## devices
List of devices that will be connected to delete local users. I'm using FQDN then, change name for IP addresses if you prefer.

## create_scripts.py
Is a code that call a jinja2 template "default_template.j2" with all default configurations and executing some loops in a yaml file "auth_vars.yml" that has some variables

## create_users.py and config_cmd
Used only for testing, creating a new users on devices using method send_config_from_file("config_cmd)to compare with variable users list on remove_users.py

## delete_users.py
This code will compare all local users on devices is in a list. If don't, all users will be remove by code.</br>
When I share the codes in github I got this file into .gitignore because has all users and password that I'm using

## net_conn.py
A module imported in files ".py" which needed a credentials to connect on devices.
