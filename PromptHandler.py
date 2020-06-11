from threading import Thread, Lock
from scapy.all import IP, TCP, UDP
from RuleTable import RuleTable
from Rule import Rule
from Controller import Controller
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
        self.controller = Controller.get_instance()
        self._stop_flag = False

    def stop_thread(self):
        self._stop_flag = True
        self.prompt_queue.put(1)
        self.mutex.release()

    def run(self):
        while True:
            self.mutex.acquire()
            packet = PromptHandler.prompt_queue.get()
            if self._stop_flag:
                print('promt thread stopped')
                break
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
            self.application_name = application_name
            self.packet = packet
            popup_text = "{} wants to connect to {}:{} ({}) on port {}.".format(str(application_name), packet.dst, packet.dport, ip_host, packet.sport)
            self.controller.show_pop_up(popup_text, self.allow_action, self.deny_action)
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

    def allow_action(self, all_ports):
        #print("Allowed", all_ports)
        packet = self.packet
        destination_port = None
        ip = packet.dst
        if UDP in packet:
            proto = 'udp'
        else:
            proto = 'tcp'
        if all_ports:
            rule_string = 'iptables -I OUTPUT -p {} -d {} -j ACCEPT'.format(proto, ip)
            os.system(rule_string)
        else:
            destination_port = packet.dport
            rule_string = 'iptables -I OUTPUT -p {} -d {} --dport {} -j ACCEPT'.format(proto, ip, destination_port)
            os.system(rule_string)
        new_rule = Rule(ip, destination_port)
        new_rule.rule_string = rule_string
        self.rule_table.add_rule(new_rule)
        self.mutex.release()
        return None


    def deny_action(self, all_ports):
        #print("Denied", all_ports)
        packet = self.packet
        destination_port = None
        ip = packet.dst
        if UDP in packet:
            proto = 'udp'
        else:
            proto = 'tcp'
        if all_ports:
            rule_string = 'iptables -I OUTPUT -p {} -d {} -j DROP'.format(proto, ip)
            os.system('iptables -I OUTPUT -p {} -d {} -j DROP'.format(proto, ip))
        else:
            destination_port = packet.dport
            rule_string = 'iptables -I OUTPUT -p {} -d {} --dport {} -j DROP'.format(proto, ip, destination_port)
            os.system('iptables -I OUTPUT -p {} -d {} --dport {} -j DROP'.format(proto, ip, destination_port))
        new_rule = Rule(ip, destination_port, is_allowed=False)
        new_rule.rule_string = rule_string
        self.rule_table.add_rule(new_rule)
        self.mutex.release()
        return None