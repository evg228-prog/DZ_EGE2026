from ipaddress import *

net = ip_network('73.148.145.65/11', False)

print(str(max(net.hosts())).replace('.', ''))

# 73159255254