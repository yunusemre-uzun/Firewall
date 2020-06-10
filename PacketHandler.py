from threading import Thread
from RuleTable import RuleTable
from PromptHandler import PromptHandler
from scapy.all import IP
from Rule import Rule
import queue
import subprocess

class PacketHandler(Thread):
    packet_queue = queue.Queue()
    print_queue = queue.Queue()

    def __init__(self):
        # Call the Thread class's init function
        Thread.__init__(self)
        self.rule_table = RuleTable.getInstance()
        self.prompt_handler = PromptHandler()
        self.prompt_handler.start()
        #localhost_rule = Rule("127.0.0.0/8", None, ip_flag=False)
        #self.rule_table.add_rule(localhost_rule)
        #t = Thread(target=self.print_packet)
        #t.start()

    def get_prompt_handler(self):
        return self.prompt_handler
    
    def run(self):
        while True:
            try:
                packet = PacketHandler.packet_queue.get()
                if packet is None:
                    print('None packet')
                    continue
                packet_payload = IP(packet.get_payload())
                ip = packet_payload.dst
                port = packet_payload.dport
                rule = self.rule_table.get_rule_of_packet_ip(ip,port)
                if rule is not None:
                    continue
                else:
                    PacketHandler.print_queue.put(packet_payload)
                    packet.accept()
                    self.prompt_handler.add_packet_to_queue(packet)
            except KeyboardInterrupt:
                break
            except AttributeError:
                packet.accept()
                continue
            except Exception:
                continue
    

    def add_packet_to_queue(self, packet):
        PacketHandler.packet_queue.put(packet)