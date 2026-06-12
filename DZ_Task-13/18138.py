from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('0') % 7 == 0

for X in [0, 128, 192, 224, 240, 248, 252, 254, 255]:
    net = ip_network(f'172.16.168.0/255.255.255.{X}', False)
    if sum(1 for i in net if f(i)) == 35:
        print(X)

# 128