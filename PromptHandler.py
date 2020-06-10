from threading import Thread, Lock
from scapy.all import IP, TCP, UDP
from RuleTable import RuleTable
from Rule import Rule
import queue
import sys
import subprocess
import os

class PromptHandler(Thread):
    prompt_queue = queue.Queue() # Thread safe queue to store user prompts

    def __init__(self):
        # Call the Thread class's init function
        Thread.__init__(self)
        self.mutex = Lock()
        self.rule_table = RuleTable.getInstance()

    def run(self):
        while True:
            self.mutex.acquire()
            packet = PromptHandler.prompt_queue.get()
            packet_payload = IP(packet.get_payload())
            try:
                port = packet_payload.sport
            except AttributeError:
                self.mutex.release()
                continue
            rule = self.rule_table.get_rule_of_packet_ip(packet_payload.dst, port)
            if rule is None:
                self.show_prompt(packet_payload)
            else:
                self.mutex.release()

    def show_prompt(self, packet):
        try:
            application_name = self.get_application_name(packet.sport)
            ip_host = self.get_host_name_of_ip(packet.dst)
            print("{} wants to connect to {}:{} ({}) on port {}.".format(str(application_name), packet.dst, packet.dport, ip_host, packet.sport))
            user_input = input()
            if user_input == 'Y':
                self.allow_action(application_name,packet)
            else:
                self.deny_action(packet)
            self.mutex.release()
        except Exception as e:
            print(e)
            self.mutex.release()

    def get_host_name_of_ip(self, ip):
        whois = subprocess.Popen("whois {}".format(ip), shell=True, stdout=subprocess.PIPE).stdout
        whois = whois.read().decode().split('\n')
        for line in whois:
            line_splitted = line.split(':')
            if line_splitted[0] == 'OrgName' or line_splitted[0] == 'netname':
                return line_splitted[1].strip()
        return ''

    def get_application_name(self, port):
        lsof = subprocess.Popen("sudo lsof -i :{}".format(port), shell=True, stdout=subprocess.PIPE).stdout
        lsof_out_lines = lsof.read().decode().split('\n')
        applications = []
        for i in range(1, len(lsof_out_lines)):
            application_name = lsof_out_lines[i].split(' ')[0]
            if application_name == '':
                continue
            applications.append(application_name)
        return applications

    def add_packet_to_queue(self, packet):
        PromptHandler.prompt_queue.put(packet)

    def allow_action(self, application_name, packet):
        port = packet.sport
        ip = packet.dst
        if UDP in packet:
            proto = 'udp'
        else:
            proto = 'tcp'
        os.system('iptables -I OUTPUT -p {} -d {} --sport {} -j ACCEPT'.format(proto, ip, port))
        new_rule = Rule(ip, port)
        self.rule_table.add_rule(new_rule)
        return None


    def deny_action(self, packet):
        port = packet.sport
        ip = packet.dst
        if UDP in packet:
            proto = 'udp'
        else:
            proto = 'tcp'
        os.system('iptables -I OUTPUT -p {} -d {} --sport {} -j DROP'.format(proto, ip, port))
        new_rule = Rule(ip, port, is_allowed=False)
        self.rule_table.add_rule(new_rule)
        return None
        