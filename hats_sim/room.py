#Room object, contains list of users and devices

import hats_sim.devices
from hats_sim.devices import device

class Room:
  """Room object"""
  def __init__(self, cfg):
    self.users = {}
    self.devices = {}
    for key, val in cfg.get('devices', {}).items():
      self.create_device(key, val)

  """Setters"""
  def add_user(self, name, user):
    self.users[name] = user
  def create_device(self, name, dev):
    self.devices[name] = device.create(dev)

  """Remove"""
  def rm_user(self, key):
    try:
      del self.users[key]
    except KeyError:
      pass

  def rm_device(self, key):
    try:
      del self.devices[key]
    except KeyError:
      pass

  """Getters"""
  def get_user(self, key):
    return self.users[key]

  def get_device(self, key):
    return self.devices[key]
  def devices_iter(self):
    return self.devices.iteritems()
  def device_names(self):
    return self.devices.keys()
  def devices(self):
    return self.devices.values()

  """Visiting Method"""
  def visit(self, graph, node, time):
    for name, user in self.users.items():
      user.visit(graph, node, time)
    for dev_id, device in self.devices.items():
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
