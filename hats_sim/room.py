#Room object, contains list of users and devices
class Room:
  """Room object"""
  def __init__(self, cfg = {}):
    self.users = []
    self.devices = []

  """Setters"""
  def add_user(self, user_id, user):
    self.users.append(user_id)
  def rm_user(self, user_id):
    self.users.remove(userID)
  def add_device(self,deviceID):
    self.devices.append(deviceID)

  """Getters"""
  def get_user(self, user_id):
    return self.users[user_id]
  def get_users(self):
    return self.users
  def get_devices(self):
    return self.devices

  """Visiting Method"""
  def visit(self, graph, time):
    for user in self.users:
      user.vist(graph, time)
    for device in self.devices:
      device.visit(graph, time)

class Door:
  """Door object, which connects between rooms"""
  def __init__(self, status = False):
    self.lock = status
  def locked(self):
    return self.lock
  def set_lock(self, status):
    self.lock = status
  def visit(self, graph, time):
    pass
