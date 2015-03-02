#Room object, contains list of users and devices
class Room:
    """Room object"""
    def __init__(self,yamlDict):
        try:
            self.users = yamlDict["users"]
        except KeyError:
            pass
        try:
            self.devices = yamlDict["devices"]
        except KeyError:
            pass

    """Setters"""
    def addUser(self,name,user):
        self.users[name] = user;
    def addDevice(self,name,user):
        self.devices[name] = user

    """Remove"""
    def removeUser(self,key):
        try:
            del self.users[key]
        except KeyError:
            pass

    def removeDevice(self, key):
        try:
            del self.devices[key]
        except KeyError:
            pass

    """Getters"""
    def getUsers(self):
        return self.users
    def getDevices(self):
        return self.devices

    """Visiting Method"""
    def visit(self, graph, time):
        for user in self.users:
            user.vist(graph,time)
        for device in self.devices:
            device.visit(graph,time)

class Door:
  def __init__(self):
    pass
  def visit(self, graph, time):
    pass
