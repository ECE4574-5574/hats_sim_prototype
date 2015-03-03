#Prerana Rane 3/2/2015

import json

class Device(object):
  def __init__(self):
    self.id = 0
    
#Light Module    
class Lights(Device):
  def __init__(self, config):
    super(Device, self).__init__()
    self.status = config.get('status', True)
    self.brightness = config.get('brightness', 1.0)
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

#Alarm Module
class Alarm(Device):
  def __init__(self, config):
    super(Device, self).__init__()
    self.alarm_status = config.get('alarm_status', True)
    self.smoke_alarm_status = config.get('smoke_alarm_status', True)
  def update(self, newConfig):
    if 'alarm_status' in newConfig:
      self.alarm_status = newConfig['alarm_status']
    if 'smoke_alarm_status' in newConfig:
      self.smoke_alarm_status = newConfig['smoke_alarm_status']
  def getStatus(self):
    return self.alarm_status
  def enableAlarm(self):
    self.alarm_status = True
  def disableAlarm(self):
    self.alarm_status = False
  def getSmokeStatus(self):
    return self.smoke_alarm_status
  def enableSmokeAlarm(self):
    self.smoke_alarm_status = True
  def disableSmokeAlarm(self):
    self.smoke_alarm_status = False
  def toJson(self):
    return json.dumps({'alarm_status' : self.alarm_status, 
                       'smoke_alarm_status' : self.smoke_alarm_status})

#HVAC Module
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

#Door Module
class doorLocks(Device):
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

#Window Module
class Windows(Device):
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
