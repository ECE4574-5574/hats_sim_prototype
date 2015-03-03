#Prerana Rane 3/2/2015

class Devices:
  def __init__(self):
    self.id = 0
    
#Light Module    
class Lights(Device):
  def __init__(self, config):
    super(Lights, self).__init__(config)
    self.status = config.get('status', True)
    self.brightness = config.get('brightness', 1.0)
  def getBrightness(self):
    return self.brightness
  def getStatus(self):
    return self.status
  def turnOn(self):
    self.brightness = 1.0
  def turnOff(self):
    self.brightness = 0.0
 
#Alarm Module
class Alarm(Device):
  def __init__(self, config):
    super(Alarm, self).__init__(config)
    self.alarm_status = config.get('alarm_status', True)
    self.smoke_alarm_status = config.get('smoke_alarm_status', True)
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

#HVAC Module
class HVAC(Device):
 def __init__(self, config):
    super(HVAC, self).__init__(config)
    self.tempCurrent = config.get('tempCurrent', 85 )
    self.humidityCurrent = config.get('humidityCurrent', 100)
    self.tempDesired = config.get('tempDesired', 80 )
    self.humidityDesired = config.get('humidityDesired', 90 )
    self.isRunning = config.get('isRunning', True)
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

#Door Module
class doorLocks(Device):
  def __init__(self, config):
    super(doorLocks, self).__init__(config)
    self.isLocked = config.get('isLocked', True )
    
    def getLockedStatus(self):
    	return self.isLocked
    def toggleDoorLocks(self):
    	self.isLocked = False

#Window Module
class Windows(Device):
  def __init__(self, config):
    super(Windows, self).__init__(config)
    self.isLocked = config.get('isLocked', True )
    self.height = config.get('height', 2 )
    self.isOpen = config.get('isOpen', True )
    
    def getLockedStatus(self):
    	return self.isLocked
    def toggleWindowLocks(self):
    	self.isLocked = False		
    def getHeight(self);
    	return self.height
    def Open(self):
    	self.isOpen = True
    def Close(self):
    	self.isOpen = False  
    def setHeight(self):
    	self.height = 1
