import os
import sys
import sysconfig
import platform
import netaddr
import networkx

# print(netaddr.glob_to_iprange())
# IPRange = 10
# # def glob_to_iprange(ipglob: str) -> IPRange

print(os.name)
print(os.fstat)

print(sys.platform.startswith("win"))
print(sys.platform)

print(sysconfig.get_platform())
# print(sysconfig.get_config_h_filename())

print("os.name                      ",  os.name)
print("sys.platform                 ",  sys.platform)
print("platform.system()            ",  platform.system())
print("sysconfig.get_platform()     ",  sysconfig.get_platform())
print("platform.machine()           ",  platform.machine())
print("platform.architecture()      ",  platform.architecture())


import networkx as nx
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("B", "D", weight=2)
G.add_edge("A", "C", weight=3)
G.add_edge("C", "D", weight=4)
nx.shortest_path(G, "A", "D", weight="weight")
['A', 'B', 'D']
