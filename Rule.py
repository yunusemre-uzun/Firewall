import datetime
from netaddr import IPAddress, IPNetwork

class Rule:
    def __init__(self, ip, port, chain='O', time=False, save_at_exit=False, ip_flag=True, is_allowed=True, rule_id=-1, rule_string=None, protocol=None):
        self.chain = chain # Indicates the chain that rule belongs to O for output, I for input
        self.time = time # Indicates the expiration date of the rule. Default no expiration date
        self.save_at_exit = save_at_exit # When its true save the rule when program exits to use later
        self.ip_flag = ip_flag # Indicates that the rule is an single IP rule or a netmask
        self.is_allowed = is_allowed
        self.ip = ip # The ip or netmask of the rule
        self.port = port
        self.rule_id = rule_id
        self.rule_string = rule_string
        self.protocol = protocol
        self.rule_id = rule_id
    
    def update_expiration_time(self, new_time):
        self.save_at_exit = True
        if new_time > datetime.datetime.now():
            self.time = new_time
        else:
            raise Exception("Invalid date")
        return True
    
    def is_expired(self):
        return self.time < datetime.datetime.now()
    
    def change_ip(self, ip_flag ,new_ip):
        self.ip_flag = ip_flag
        self.ip = new_ip
    
    def address_in_network(self, ip):
        '''Is an address in a network'''
        if self.ip_flag:
            return self.ip == ip
        else:
            return IPAddress(ip) in IPNetwork(self.ip)

    def get_parameters(self):
        if self.is_allowed:
            allowed_str = "Allowed"
        else:
            allowed_str = "Denied"
        return [self.rule_id, self.ip, self.port, self.protocol, allowed_str]

    