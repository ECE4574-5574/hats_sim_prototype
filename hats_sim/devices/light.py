#!/usr/env python
# Author: Prerana Rane 3/2/2015

from device import Device
import json

#Light Module
class Light(Device):
  def __init__(self, config):
    super(Device, self).__init__()
    self.status = config.get('status', True)
    self.brightness = config.get('brightness', 1.0)
    print self.status
  def update(self, newConfig):
    if 'status' in newConfig:
      self.status = newConfig['status']
    if 'brightness' in newConfig:
      self.brightness = newConfig['brightness']
  def getBrightness(self):
    return self.brightness
  def getStatus(self):
    return self.status
  def turnOn(self):
    self.brightness = 1.0
  def turnOff(self):
    self.brightness = 0.0
  def toJson(self):
    return json.dumps({'status' : self.status,
                       'brightness' : self.brightness})