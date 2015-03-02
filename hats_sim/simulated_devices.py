class HatsSimDevice:
	def __init__(self, deviceID):
		self.deviceID = deviceID
	
	def getID(self):
		return self.deviceID

class LightSwitch(HatsSimDevice):
	def __init__(self, deviceID):
		HatsSimDevice.__init__(self, deviceID)
		self.on = False
	
	def __init__(self, deviceID, initSetting):
		HatsSimDevice.__init__(self, deviceID)
		self.on = initSetting

	def getState(self):
		return self.on

	def switch(self, newState):
		self.on = newState


class Thermostat(HatsSimDevice):
	def __init__(self, deviceID):
	        HatsSimDevice.__init__(self, deviceID)	
		self.tempF = 65

	def __init__(self, deviceID, tempF):
		HatsSimDevice.__init__(self, deviceID)
		self.tempF = tempF

	def getTempF(self):
		return self.tempF

	def setTempF(self, tempF):
		self.tempF = tempF
