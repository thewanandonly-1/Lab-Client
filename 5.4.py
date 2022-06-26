from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.102',  #Your Server IP
    'username': 'wan', #your Server Username
    'password': '12345', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('sudo apt-get update')
print (output)
