from Rule import Rule

class RuleTable():
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if RuleTable.__instance == None:
            RuleTable()
        return RuleTable.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if RuleTable.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RuleTable.__instance = self
            self.table = []

    def get_rule_of_packet_ip(self, ip, port):
        for rule in self.table:
            if rule.address_in_network(ip) and rule.port == port:
                return rule
        return None
    
    def add_rule(self, rule:Rule):
        self.table.append(rule)

    def remove_rule(self, rule:Rule):
        pass

    def import_rules(self):
        pass

    def save_rules(self):
        pass
