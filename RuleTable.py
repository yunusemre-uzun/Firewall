from Rule import Rule
import os

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
            self.table = {}

    def get_rule_of_packet_ip(self, ip, port):
        for rule in self.table.values():
            if rule.port is None:
                if rule.address_in_network(ip):
                    return rule
            if rule.address_in_network(ip) and rule.port == port:
                return rule
        return None
    
    def add_rule(self, rule:Rule):
        rule.rule_id = len(self.table.keys()) + 1
        self.table[rule.rule_id] = rule

    def remove_rule(self, rule_id):
        rule = self.table[rule_id]
        os.system(rule.rule_string.replace('-I', '-D'))
        del self.table[rule_id]

    def remove_all_rules(self):
        for rule_id in list(self.table.keys()):
            self.remove_rule(rule_id)
        
    def import_rules(self):
        pass

    def save_rules(self):
        pass
