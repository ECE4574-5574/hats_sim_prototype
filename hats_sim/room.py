#Room object, contains list of users and devices
class Room:
  """Room object"""
  def __init__(self, cfg = {}):
    self.users = []
    self.devices = []

  """Setters"""
  def add_user(self, id, user):
    self.users.append(userID)
  def rm_user(self, userID):
    self.users.remove(userID)
  def add_device(self,deviceID):
    self.devices.append(deviceID)

  """Getters"""
  def get_user(self):
    return self.users
  def get_devices(self):
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
