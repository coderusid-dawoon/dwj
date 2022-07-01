from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl

# Get all the Datacenter from vCenter inventory and print its name
# Below is Python 2.7.x code, which can be easily converted to python 3.x version

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host="10.192.3.2", user="Administrator@vsphere.local", pwd="$h1vKamal",sslContext=s)
content=si.content

# Method that populates objects of type vimtype
def get_all_objs(content, vimtype):
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for managed_object_ref in container.view:
        obj.update({managed_object_ref: managed_object_ref.name})
    return obj

#Calling above method
getdcs=get_all_objs(content, [vim.Datacenter])

#Iterating each datacenter object and printing its name
for datacenter in getdcs:
    print(datacenter.name)