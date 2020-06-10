from Firewall import Firewall
from frontend.main import MyApp
from Controller import Controller

if __name__ == "__main__":
    frontend = MyApp()
    controller = Controller.get_instance(frontend)
    firewall = Firewall()
    firewall.start()
    frontend.run()
