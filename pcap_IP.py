# pacp 파일의 IP 확인  및 buf

import dpkt
import datetime
import socket

filename='D:/002.pcap'
#filename='C:/tool/test.pcap'

'''
def mac_addr(address):
    return ':'.join('%02x' % ord(b) for b in address)
'''
with open(filename, 'rb') as f:
    pcap = dpkt.pcap.Reader(f)

    var = 100

    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        var = var - 1

        if var == 0:
            break

        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue

        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue

        print('Timestamp: ', timestamp)
 #       print('Ethernet Frame: ', mac_addr(eth.src), ' -> ', mac_addr(eth.dst), eth.type)
        #print('IP: %s -> %s len=%d buf : %s \n' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len, eth))
        print('IP:%s->%s len=%d\n' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len))
        print('buf:%s\n' % eth)