from threading import Thread
from RuleTable import RuleTable
from PromptHandler import PromptHandler
import queue
import subprocess

class PacketHandler(Thread):
    packet_queue = queue.Queue()

    def __init__(self):
       # Call the Thread class's init function
       Thread.__init__(self)
       self.rule_table = RuleTable.getInstance()
       self.prompt_handler = PromptHandler()

    def run(self):
        while True:
            try:
                packet = PacketHandler.packet_queue.get()
                #port = packet.sport
                ip = packet.dst
                rule = self.rule_table.get_rule_of_packet_ip(ip)
                if rule is not None:
                    if rule.is_allowed:
                        packet.accept()
                    else:
                        packet.drop()
                else:
                    self.prompt_handler.add_packet_to_queue(packet)
                    packet.accept()
                #host_name = get_host_name(ip)
            except KeyboardInterrupt:
                break
            except Exception:
                continue
    
    def print_packages(self, packet):
        print(packet.dst, packet.sport, self.get_application_name(packet.sport))

    def get_application_name(self, port):
        lsof = subprocess.Popen("sudo lsof -i :{}".format(port), shell=True, stdout=subprocess.PIPE).stdout
        lsof_out_lines = lsof.split('\n')
        applications = []
        for i in range(1, len(lsof_out_lines)):
            application_name = lsof_out_lines[i].split(' ')[0]
            if application_name == '':
                continue
            applications.append(application_name)
        return applications
    
    def add_packet_to_queue(self, packet):
        PacketHandler.packet_queue.put(packet)