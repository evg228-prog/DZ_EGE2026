from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224')

cnt = 0

for i in net:
    i = f'{int(i):032b}'
    if int(i.count('1')) % 4 == 0:
        cnt += 1
print(cnt)

# 10