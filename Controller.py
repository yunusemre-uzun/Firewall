class Controller:
    __instance = None

    @staticmethod
    def get_instance(frontend=None, firewall=None):
        if Controller.__instance is None:
            Controller(frontend, firewall)
        return Controller.__instance

    def __init__(self, frontend, firewall):
        Controller.__instance = self
        self.frontend = frontend
        self.firewall = firewall
    
    def show_pop_up(self, pop_up_text, allow_action, deny_action):
        self.frontend.show_pop_up(pop_up_text, allow_action, deny_action)
    
    def connection_allowed(self):
        return None

        

