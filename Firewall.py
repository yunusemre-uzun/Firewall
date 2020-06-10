from netfilterqueue import NetfilterQueue
from PacketHandler import PacketHandler
from RuleTable import RuleTable
import socket
import sys
import os
import time
import threading
import queue
import subprocess


class Firewall(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.packet_handler = PacketHandler()
        self.nfqueue = NetfilterQueue()
        self.rule_table = RuleTable.getInstance()
        #Add nfqueue to ip table output chain
        self.add_iptable_rule()
        #Get previous user rules from file
    
    def add_iptable_rule(self):
        os.system("iptables -A OUTPUT -j NFQUEUE --queue-num 1")


    def save_packet_to_queue(self, pkt):
        self.packet_handler.add_packet_to_queue(pkt)


    def get_host_name(self, ip_address):
        return socket.gethostbyaddr(ip_address)[0]

        
    def exit(self):
        self.rule_table.save_rules()
        #Remove nfqueue from ip table output chain
        os.system("iptables -D OUTPUT -j NFQUEUE --queue-num 1")
        self.nfqueue.unbind()
        sys.exit(1)
    
    def run(self):
        self.packet_handler.start()
        self.nfqueue.bind(1, self.save_packet_to_queue)
        try:
            self.nfqueue.run()
        except KeyboardInterrupt:
            self.exit()
        except Exception:
            self.exit()
