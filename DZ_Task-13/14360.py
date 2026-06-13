from ipaddress import *

for mask in range(33):
    net = ip_network(f'153.202.16.37/{mask}', False)
    if str(net.network_address) == '153.202.16.32':
        print(net.netmask)

# 503