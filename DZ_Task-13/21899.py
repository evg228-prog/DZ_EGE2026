from ipaddress import *

net = ip_network('98.81.154.195/14', False)

print(str(max(net.hosts())).replace('.', ''))