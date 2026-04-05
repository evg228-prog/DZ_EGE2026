from ipaddress import *

def f(i):
    i = f'{int(i):032b}'
    return i[16:24].count('0') > i[24:].count('0')

cnt = 0

for A in range(256):
    ip = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip}/255.255.255.224', False)
    if ip in net.hosts() and all(f(ip) for ip in net.hosts()):
        cnt += 1
print(cnt)

# 120