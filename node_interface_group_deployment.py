# RUN INSTRUCTIONS:
# This is a deployment file to deploy interface groups fo Linux servers which are using two NIC cards.
# Data is contained in the data file, xkubnodes.csv
# The values of 'nic1' and 'nic2' are derived from the LLDP information received from the card
# NIC1 = enp4s0f0
# NIC2 = enp5s0f0
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
