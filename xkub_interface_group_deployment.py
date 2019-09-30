# RUN INSTRUCTIONS:
# python3 xkub_interface_group.py

"""
bcf_ops.deployXkubInterfaceGroup(name,mode,host,nic1,nic2)
CSV value table
0=name
1=mode
2=host
3=nic1
4=nic2
"""



import csv
from bcf_ops import bcf_ops


csv_source = open('xkubnodes.csv')
deployment_reader = csv.reader(csv_source)
deployment = list(deployment_reader)

# print(deployment)



for i in deployment:
        name = f'{i[0]}'
        mode = f'{i[1]}'
        host = f'{i[2]}'
        nic1 = f'{i[3]}'
        nic2 = f'{i[4]}'
        bcf_ops.deployXkubInterfaceGroup(name,mode,host,nic1,nic2)
