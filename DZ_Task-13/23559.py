from ipaddress import *

net = ip_network('102.162.200.51/24', False)
print(eval(str(max(net.hosts())).replace('.', '+')))

# 718