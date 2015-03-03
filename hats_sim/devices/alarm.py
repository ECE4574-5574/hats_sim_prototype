#Alarm Module
from device import Device
import json

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