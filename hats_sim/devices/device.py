#Prerana Rane 3/2/2015

import devices
import json
import requests as req

class Device(object):
  def __init__(self):
    self.id = 0
  def visit(self, graph, node, time):
    pass

def create(dev):
  result = None
  if dev['type'] in devices.__all__:
    module_ = __import__('devices.' + dev['type'])
    d_mod_ = getattr(module_, dev['type'])
    instance = dev.get('instance', dev['type']).title()
    class_ = getattr(d_mod_, instance)
    result = class_(dev)
  return result
