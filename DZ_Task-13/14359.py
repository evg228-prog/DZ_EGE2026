from ipaddress import *

ip_1 = ip_address('157.127.172.56')
ip_2 = ip_address('157.127.191.78')

def f(i):
    i = f'{int(i):032b}'
    return i.count('1')

for mask in range(16, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 not in net.hosts():
        print(mask)
        break

# 20