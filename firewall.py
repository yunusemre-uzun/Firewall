from netfilterqueue import NetfilterQueue
from scapy.all import IP
from filter import Filter
import socket
import sys
import os
import time
import threading
import queue
import subprocess

print_queue = queue.Queue()

def print_and_accept(pkt):
    global print_queue
    #print(pkt.get_payload().decode())
    packet_payload = IP(pkt.get_payload())
    #ip.show()
    print_queue.put(packet_payload)
    #print_packet(packet_payload)
    pkt.accept()
    
    

def print_packet():
    while True:
        try:
            packet = print_queue.get()
            port = packet.sport
            ip = packet.dst
            if ip == "188.122.81.135":
                continue
            host_name = get_host_name(ip)
            if host_name == "localhost":
                continue
            print(ip)
            print(port)
            print(get_application_name(port))
            print(host_name)
        except KeyboardInterrupt:
            break
        except Exception:
            continue

def get_application_name(port):
    lsof = subprocess.Popen("sudo lsof -i :{}".format(port), shell=True, stdout=subprocess.PIPE).stdout
    lsof_out = lsof.read().decode()
    #print(lsof_out)
    '''
    lsof_out_lines = lsof_out.split('\n')
    applications = []
    for i in range(1, len(lsof_out_lines)):
        application_name = lsof_out_lines[i].split(' ')[0]
        if application_name == '':
            continue
        applications.append(application_name)
    '''
    return lsof_out

def get_host_name(ip_address):
    return socket.gethostbyaddr(ip_address)[0]

def load_user_settings():
    pass

def init():
    #Add nfqueue to ip table output chain
    os.system("iptables -A OUTPUT -j NFQUEUE --queue-num 1")
    #Get user settings from file
    load_user_settings()
    #time.sleep(3)

def main():
    t = threading.Thread(target=print_packet)
    t.start()
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, print_and_accept)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        exit()
    except Exception:
        exit()


def exit():
    #Remove nfqueue from ip table output chain
    os.system("iptables -D OUTPUT -j NFQUEUE --queue-num 1")
    nfqueue.unbind()
    sys.exit(1)

if __name__ == "__main__":
    init()
    main()
