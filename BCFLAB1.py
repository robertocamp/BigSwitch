from imp_common.encryption import Encryption

"""
settings file will  retrieve the current API password
"""
# the following function is NOT defined in this repo, sorry.
encrypted = 'gAAAAABdjho8gym25XKZb49H87aN1lLaLIYLhapWMA5bmuu27PcnGNuuAk68G-nDzmmvFKj5ThEKhCGmyda2HCZbVqtVMUI3IA=='
e = Encryption(env='prod')
api = e.decrypt(encrypted)


POD =  "BCFLAB1"
URL = "https://10.226.195.224:8443"
USER = "admin"
AUTH = api


