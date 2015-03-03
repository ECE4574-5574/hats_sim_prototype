#Window Module
from device import Device
import json

class Window(Device):
  def __init__(self, config):
    super(Device, self).__init__()
    self.isLocked = config.get('isLocked', True )
    self.height = config.get('height', 2 )
    self.isOpen = config.get('isOpen', True )
  def update(self, newConfig):
    if 'isLocked' in newConfig:
      self.isLocked = newConfig['isLocked']
    if 'height' in newConfig:
      self.height = newConfig['height']
    if 'isOpen' in newConfig:
      self.height = newConfig['isOpen']
  def getLockedStatus(self):
    return self.isLocked
  def toggleWindowLocks(self):
    self.isLocked = False
  def getHeight(self):
    return self.height
  def Open(self):
    self.isOpen = True
  def Close(self):
    self.isOpen = False
  def setHeight(self):
    self.height = 1
  def toJson(self):
    return json.dumps({'isLocked' : self.isLocked,
                       'height' : self.height,
                       'isOpen' : self.isOpen})