#Room object, contains list of users and devices
class Room:
    """Room object"""
    def __init__(self):
        self.users = []
        self.devices = []

    """Setters"""
    def addUser(self,userID):
        self.users.append(userID)
    def addDevice(self,deviceID):
        self.devices.append(deviceID)

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
