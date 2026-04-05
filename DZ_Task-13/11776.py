from ipaddress import *

net = ip_network('235.86.56.0/255.255.248.0', False)

cnt = 0

for i in net:
    i = f'{int(i):032b}'
    if int(i) % 100 == 11:
        cnt += 1
print(cnt)

# 512