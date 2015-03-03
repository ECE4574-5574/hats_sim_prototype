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
    def get_user(self, key):
      return self.users[key]

    def get_device(self, key):
      return self.devices[key]

    """Visiting Method"""
    def visit(self, graph, node, time):
      for user in self.users:
        user.vist(graph, node, time)
      for device in self.devices:
        device.visit(graph, node, time)

class Door:
  """Door object, which connects between rooms"""
  def __init__(self, status = False):
    self.lock = status
  def locked(self):
    return self.lock
  def set_lock(self, status):
    self.lock = status
  def visit(self, graph, source, target, time):
    pass
