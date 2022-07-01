from pyVmomi import vim
from pyVim.connect import SmartConnectNoSSL, Disconnect
from math import log, floor

si = SmartConnectNoSSL(
            host='192.168.52.129',
            user='root',
            pwd='Dlxpzm123!')

content = si.RetrieveContent()
perfManager = content.perfManager

# counterInfo = {}
# # {'cpu.usage.none': 0, 'cpu.usage.average': 1, 'cpu.usage.maximum': 2, ... }
# for c in perfManager.perfCounter:
#     prefix = c.groupInfo.key
#     fullName = c.groupInfo.key + "." + c.nameInfo.key + "." + c.rollupType
#     counterInfo[fullName] = c.key

def convertMemory(sizeBytes):
    name = ("B", "KB", "MB", "GB", "TB", "PB")
    base = int(floor(log(sizeBytes, 1024)))
    power = pow(1024,base)
    size = round(sizeBytes/power,2)
    return "{}{}".format(floor(size),name[base])

hosts = content.viewManager.CreateContainerView(content.rootFolder,[vim.HostSystem],True)
for host in hosts.view:
    # Print the hosts cpu details
    print(host.hardware.cpuInfo)
    # convert CPU to total hz to ghz times numCpuCores
    print("CPU:", round(((host.hardware.cpuInfo.hz/1e+9)*host.hardware.cpuInfo.numCpuCores),0),"GHz")
    #covert the raw bytes to readable size via convertMemory
    print("Memory:", convertMemory(host.hardware.memorySize))

    print("Name:", host.name)

# print(counterInfo)

# container = content.rootFolder
# viewType = [vim.VirtualMachine]
# recursive = True

# containerView = content.viewManager.CreateContainerView(container, viewType, recursive)
# children = containerView.view

# for child in children:
#     # Get all available metric IDs for this VM
#     counterIDs = [m.counterId for m in
#                   perfManager.QueryAvailablePerfMetric(entity=child)]

#     # Using the IDs form a list of MetricId
#     # objects for building the Query Spec
#     metricIDs = [vim.PerformanceManager.MetricId(counterId=c,
#                                                  instance="*")
#                  for c in counterIDs]

#     # Build the specification to be used
#     # for querying the performance manager
#     spec = vim.PerformanceManager.QuerySpec(maxSample=1,
#                                             entity=child,
#                                             metricId=metricIDs)
#     # Query the performance manager
#     # based on the metrics created above
#     result = perfManager.QueryStats(querySpec=[spec])

#     print(result, child.summary.config.name)