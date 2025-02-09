import os
import nmap

scanner = nmap.PortScanner()

scanner.scan('', '21-80')

for host in scanner.all_hosts():
    print('host : %s' % (scanner[host].hostname()))
    print('state : %s' % scanner[host].state())
    for proto in scanner[host].all_protocols():
         print('------------------')
         print('protocol : %s' % proto)
    
         lport = scanner[host] [proto].keys()
         
         for port in lport:
             print ('port : %s\tstate : %s' % (port, scanner[host] [proto] [port] ['state']))
             
             
