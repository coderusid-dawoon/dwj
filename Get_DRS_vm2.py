# Author: Vikas Shitole
# Website: www.vThinkBeyondVM.com
# Product: vCenter server/vSphere DRS rules
# Description: Python script to get associated DRS rules for a Virtual Machine (from DRS cluster)
# Reference:http://vthinkbeyondvm.com/pyvmomi-tutorial-how-to-get-all-the-core-vcenter-server-inventory-objects-and-play-around/
# How to setup pyVmomi environment?: http://vthinkbeyondvm.com/how-did-i-get-started-with-the-vsphere-python-sdk-pyvmomi-on-ubuntu-distro/


from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl

s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode=ssl.CERT_NONE
c= SmartConnect(host="10.161.2.3", user="Administrator@vsphere.local", pwd="VMware1!",sslContext=s)
content=c.content

# "vimtype" 과 일치하는 모든 객체를 가져옵니다.
def get_all_objs(content, vimtype):
        obj = {}
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj

# 인벤토리 내부의 입력 VM 스캔
# 모든 VM들을 가져오고 인벤토리 내에서 입력 VM을 사용할 수 있는지 여부를 확인하고 마지막으로 일치하는 조건으로 목록을 반환합니다.
vmName="NTP-1"
vmToScan = [vm for vm in get_all_objs(content,[vim.VirtualMachine]) if vmName  == vm.name]
if len(vmToScan) == 0:
        print("인벤토리에서 VM을 찾을수 없습니다. 전달된 VM 이름을 확인하십시오")
        quit()

# 위 함수와 방식은 동일하며 클러스터를 스캔합니다.
clusterName="Cluster-India"
cluster = [cluster for cluster in get_all_objs(content,[vim.ClusterComputeResource]) if clusterName  == cluster.name]
if len(cluster) == 0:
        print("인벤토리에서 Cluster를 찾을수 없습니다. 전달된 Cluster 이름을 확인하십시오")
        quit()

# 이제 입력 VM을 매개변수로 전달하여 입력 클러스터에서 메서드를 호출할 수 있으며 입력 VM과 연결된 규칙 개체의 배열을 반환합니다.
ClusterRuleInfo=cluster[0].FindRulesForVm(vmToScan[0])

# 이제 규칙 개체를 반복하고 규칙 이름을 인쇄하십시오.
if len(ClusterRuleInfo) != 0:
        for rule in ClusterRuleInfo:
                print(rule.name)
else:
        print("There is no DRS rule associated with input VM")
