from threading import Thread
import queue

class PromptHandler(Thread):
    prompt_queue = queue.Queue() # Thread safe queue to store user prompts

    def __init__(self):
        # Call the Thread class's init function
        Thread.__init__(self)

    def run(self):
        pass

    def add_packet_to_queue(self, packet):
        PromptHandler.prompt_queue.put(packet)