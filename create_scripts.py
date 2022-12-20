#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader

#Import YAML from PyYAML
import yaml

with open("devices")as f:
    devices_list = f.read().splitlines()

def create_scripts():
    #Load data from YAML file into Python dictionary
    config = yaml.full_load(open('./auth_vars.yml'))

    #Load Jinja2 template
    env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)

    for i in devices_list:
        template = env.get_template(f'default_template.j2')
        output = template.render(config)
        scriptFile = open(f'config_default.cfg', "w+")
        scriptFile.write(output)
        print(f'Created script FileName config_default.cfg')
        print(output)

create_scripts()