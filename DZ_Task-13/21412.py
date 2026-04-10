from ipaddress import *

print(str(ip_network('143.168.72.213/28', False).broadcast_address - 1).replace('.', ''))

# 14316872222