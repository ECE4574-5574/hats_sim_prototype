#HVAC Module
from device import Device
import json

class HVAC(Device):
  def __init__(self, config):
    super(Device, self).__init__()
    self.tempCurrent = config.get('tempCurrent', 85 )
    self.humidityCurrent = config.get('humidityCurrent', 100)
    self.tempDesired = config.get('tempDesired', 80 )
    self.humidityDesired = config.get('humidityDesired', 90 )
    self.isRunning = config.get('isRunning', True)
  def update(self, newConfig):
    if 'tempCurrent' in newConfig:
      self.tempCurrent = newConfig['tempCurrent']
    if 'humidityCurrent' in newConfig:
      self.humidityCurrent = newConfig['humidityCurrent']
    if 'tempDesired' in newConfig:
      self.tempDesired = newConfig['tempDesired']
    if 'humidityDesired' in newConfig:
      self.humidityDesired = newConfig['humidityDesired']
    if 'isRunning' in newConfig:
      self.isRunning = newConfig['isRunning']
  def getRunningStatus(self):
    return self.isRunning
  def getTemperature(self):
    return self.tempCurrent
  def setTemperature(self):
    self.tempCurrent= self.tempDesired
  def getHumidty(self):
    return self.humidityCurrent
  def setHumidity(self):
   self.humidityCurrent = self.humidityDesired
  def visit(self, graph, node, time):
    if isRunning:
      temp = getTemperature()
      if temp != self.tempDesired:
        setTemperature()
      humidity = getHumidity()
      if humidity != self.humidityDesired:
        setHumidity()
  def toJson(self):
    return json.dumps({'tempCurrent' : self.tempCurrent,
                       'humidityCurrent' : self.humidityCurrent,
                       'tempDesired' : self.tempDesired,
                       'humidityDesired' : self.humidityDesired,
                       'isRunning' : self.isRunning})