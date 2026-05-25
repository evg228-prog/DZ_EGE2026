from ipaddress import *

net = ip_network('68.203.243.87/19', False)
print(eval(str(max(net.hosts())).replace('.', '+')))

# 780