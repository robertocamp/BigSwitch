from imp_common.encryption import Encryption

"""
settings file will go to imp_common and retrieve the current API PASSWORD
"""

encrypted = 'gAAAAABdjho8gym25XKZb49H87aN1lLaLIYLhapWMA5bmuu27PcnGNuuAk68G-nDzmmvFKj5ThEKhCGmyda2HCZbVqtVMUI3IA=='
e = Encryption(env='prod')
api = e.decrypt(encrypted)


POD =  "BCFLAB1"
#controller_ip = "10.219.0.69"
URL = "https://10.226.195.224:8443"
USER = "admin"
AUTH = api


