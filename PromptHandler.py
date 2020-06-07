from threading import Thread, Lock
from scapy.all import IP
from ui.test2_window import Ui_MainWindow
from PyQt5 import QtWidgets
import queue
import sys
import subprocess

class PromptHandler(Thread):
    prompt_queue = queue.Queue() # Thread safe queue to store user prompts

    def __init__(self):
        # Call the Thread class's init function
        Thread.__init__(self)
        self.mutex = Lock()

    def run(self):
        while True:
            self.mutex.acquire()
            packet = PromptHandler.prompt_queue.get()
            packet_payload = IP(packet.get_payload())
            #print(packet_payload.show())
            self.show_prompt(packet_payload)

    def show_prompt(self, packet):
        try:
            application_name = self.get_application_name(packet.sport)
            print("{} wants to connect to {} on port {}.".format(str(application_name), str(packet.dst), str(packet.sport)))
            self.mutex.release()
        except Exception:
            self.mutex.release()

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

    def allow_action(self):
        print("Allowed")
        self.mutex.release()

    def close_action(self):
        print("Closed")
        self.mutex.release()

    def deny_action(self):
        print("Denied")
        self.mutex.release()
        