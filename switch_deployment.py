# RUN INSTRUCTIONS:
# python3 switch_deployment.py

"""
bcf_ops.deploySwitch(switchname, role, leafgroup, mac)
CSV value table
0=switchname
1=role 
2=leafgroup  ! NOTE--SPINE LEAFGROUP SET TO "none"
3=mac
"""



import csv
from bcf_ops import bcf_ops


csv_source = open('switch_manifest.csv')
deployment_reader = csv.reader(csv_source)
deployment = list(deployment_reader)

# print(deployment)



for i in deployment:
    if i[1]=="leaf":
        switchname = f'{i[0]}'
        role = f'{i[1]}'
        leafgroup = f'{i[2]}'
        mac = f'{i[3]}'
        bcf_ops.deployLeaf(switchname, role, leafgroup, mac)


    else:
        switchname = f'{i[0]}'
        role = f'{i[1]}'
        mac = f'{i[3]}'
        bcf_ops.deploySpine(switchname, role, mac)
