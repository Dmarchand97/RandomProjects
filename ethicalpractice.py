import nmap
ns = nmap.PortScanner()

print(ns.nmap_version())

ns.scan('192.168.1.55/24', '1-200', '-v --version-all')

#print(ns.scaninfo())

#print(ns.csv())

print(ns.scanstats())
#show hosts
#print(ns.all_hosts())

#print(ns['192.168.1.55'].state)
#to find the status of IP

#print(ns['192.168.1.55'].all_protocols())
#specific protocol

#print(ns['192.168.1.55']['tcp'].keys())

print(ns['192.168.1.55'].has_tcp(80))