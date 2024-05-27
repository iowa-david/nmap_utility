
import nmap 

nm = nmap.PortScanner() 

  
# scan a target host for open ports 

nm.scan('localhost', arguments='--top-ports 1000') 

  
# print the state of the ports 

for host in nm.all_hosts(): 

    print('Host : %s (%s)' % (host, nm[host].hostname())) 

    print('State : %s' % nm[host].state()) 

    for proto in nm[host].all_protocols(): 

        print('Protocol : %s' % proto) 

        ports = nm[host][proto].keys() 

        for port in ports: 

            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


#results = nmap.nmap_dns_brute_script("localhost")

#print(results)
