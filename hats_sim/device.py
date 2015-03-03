#Prerana Rane 3/2/2015

class Devices:
  def __init__(self):
    self.id = 0
    
#Light Module    
class Lights(Device):
  def __init(self, config):
    super(Lights, self).__init__(config)
    self.status = config.get('status', True)
    self.brightness = config.get('brightness', 1.0)
  def getBrightness():
    return self.brightness
  def getStatus():
    return self.status
  def turnOn():
    self.brightness = 1.0
  def turnOff():
    self.brightness = 0.0
 
#Alarm Module
class Alarm(Device):
def __init(self, config):
    super(Alarm, self).__init__(config)
    self.alarm_status = config.get('alarm_status', True)
    self.smoke_alarm_status = config.get('smoke_alarm_status', True)
  def getStatus():
    return self.alarm_status
  def enableAlarm():
    self.alarm_status = True
  def disableAlarm():
    self.alarm_status = False
  def getSmokeStatus():
    return self.smoke_alarm_status
  def enableSmokeAlarm():
    self.smoke_alarm_status = True
  def disableSmokeAlarm():
    self.smoke_alarm_status = False

#HVAC Module
class HVAC(Device):
 def __init(self, config):
    super(HVAC, self).__init__(config)
    self.tempCurrent = config.get('tempCurrent', 85 )
    self.humidityCurrent = config.get('humidityCurrent', 100)
    self.tempDesired = config.get('tempDesired', 80 )
    self.humidityDesired = config.get('humidityDesired', 90 )
    self.isRunning = config.get('isRunning', True)
  def getRunningStatus():
    return self.isRunning
    if isRunning:
    	def getTemperature():
    	  return self.tempCurrent
    	  if tempCurrent!= tempDesired
    	  	def setTemperature():
    	  		tempCurrent= tempDesired
        
    	def getHumidty():
    	  return self.humidityCurrent
    	  if humidityCurrent!= humidityDesired
    	  	def setHumidity():
    	  		humidityCurrent= humidityDesired

#Door Module
class doorLocks(Device):
def __init(self, config):
    super(doorLocks, self).__init__(config)
    self.isLocked = config.get('isLocked', True )
    
    def getLockedStatus():
    return self.isLocked
    	if isLocked:
    		def toggleDoorLocks():
    		 self.isLocked = False

#Window Module
class Windows(Device):
def __init(self, config):
    super(Windows, self).__init__(config)
    self.isLocked = config.get('isLocked', True )
    self.height = config.get('height', 2 )
    self.isOpen = config.get('isOpen', True )

    
    def getLockedStatus():
    return self.isLocked
    	if isLocked:
    		def toggleWindowLocks():
    		 self.isLocked = False
    def getHeight();
    return self.height
    def Open():
    self.isOpen = True
    def Close():
    self.isOpen = False  
    def setHeight():
    self.height = 1
