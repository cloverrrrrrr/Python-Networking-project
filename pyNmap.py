import nmap

nmap = nmap.PortScanner()

target = "45.33.32.156" #ip yang ingin di scan
options = "-sV -sC scan_results"

nmap.scan(target, arguments=options)

for host in nmap.allhosts():
    print("Host: %s (%s)" % (host, nmap[host].hostname()))
    print("State: %s" % nmap[host].state())
    for protocol in nmap[host].all_protocols():
        print("protocol: %s" % protocol)
        port_info = nmap[host][protocol]
        for port, state in port_info.items():
            print("Port: %s \tState: %s" % (port, state))