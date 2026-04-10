from ipaddress import *

net = ip_network('45.172.106.203/255.255.252.0', False)

print(str(net.broadcast_address - 1).replace('.', ''))

# 45172107254