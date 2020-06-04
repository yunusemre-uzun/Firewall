class Filter():
    def __init__(self, destinations, hosts):
        self.__destinations = destinations
        self.__hosts = hosts

    def check_permission_output(self, ip):
        return self.__destinations[ip]
    
    def check_permission_input(self, ip):
        return self.__hosts[ip]
    
    def allow_host(self, ip):
        self.__hosts[ip] = True
    
    def reject_host(self, ip):
        self.__hosts[ip] = False

    def allow_destination(self, ip):
        self.__destinations[ip] = True
    
    def reject_destination(self, ip):
        self.__destinations[ip] = False