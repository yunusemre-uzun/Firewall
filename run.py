from Firewall import Firewall
from frontend.main import MyApp

if __name__ == "__main__":
    firewall = Firewall()
    firewall.run()
    MyApp().run()
    
