from ipaddress import *

net = ip_network('68.203.243.87/255.255.224.0', False)
last_ip = list(net.hosts())[-1]

print(eval(str(last_ip).replace('.', '+')))

# 780