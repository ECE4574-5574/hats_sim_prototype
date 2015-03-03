#Door Module
from device import Device
import json

class Lock(Device):
  def __init__(self, config):
    super(Device, self).__init__()
    self.isLocked = config.get('isLocked', True )
  def update(self, newConfig):
    if 'isLocked' in newConfig:
      self.isLocked = newConfig['isLocked']
  def getLockedStatus(self):
    return self.isLocked
  def toggleDoorLocks(self):
    self.isLocked = False
  def toJson(self):
    return json.dumps({'isLocked' : self.isLocked})