import dpkt

filename='D:/002.pcap'

f = open(filename, 'rb')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.sll.SLL(buf)
    ip = eth.data
#    tcp = ip.data
    print(eth)
    print(ip)

    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    try:
        if (tcp.dport == 80 or tcp.dport == 443) and len(tcp.data) > 0:
            request = dpkt.http.Request(tcp.data)
    except:
        pass

f.close()