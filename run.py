from Firewall import Firewall
from frontend.main import MyApp
from Controller import Controller
import sys
import time

if __name__ == "__main__":
    frontend = MyApp()
    controller = Controller.get_instance(frontend)
    firewall = Firewall()
    firewall.daemon = True
    firewall.start()
    frontend.run()
    firewall.exit()
    print('Firewall exited')
    sys.exit(1)
