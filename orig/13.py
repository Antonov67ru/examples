from ipaddress import *
net = ip_network('106.184.0.0/255.248.0.0', 0)
k = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 2 != 0:
        k += 1
print(k)