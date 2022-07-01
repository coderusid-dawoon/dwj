from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl

# Get all the datastores from vCenter inventory and print its name
# Below is Python 2.7.x code, which can be easily converted to python 3.x version

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host="192.168.52.129", user="root", pwd="Dlxpzm123!",sslContext=s)
content=si.content

# Method that populates objects of type vimtype
def get_all_objs(content, vimtype):
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for managed_object_ref in container.view:
        obj.update({managed_object_ref: managed_object_ref.name})
    return obj

#Calling above method
getdatastores=get_all_objs(content, [vim.HostSystem])

#Iterating each datastore object and printing its name
for datastore in getdatastores:
    print(datastore.name)