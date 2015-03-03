#Prerana Rane 3/2/2015

import devices
import json

class Device(object):
  def __init__(self):
    self.id = 0
  def visit(self, graph, node, time):
    pass
  def process_device(self, graph, node, time):
    """Processes the device in the node and constructs the respective API calls"""
    self.excecute_call(graph, node, time)

  def execute_call(self, graph, node, time):
    url = 'https://<server_IP>/user/home/devices/' + str(self.id)  
    payload = {'currentState' : state,
         'requestedState' : reqState,
         'graph' : str(graph),
         'node' : str(node),
         'time' : str(time)}
    headers = {'User-Agent' : '',
      'Content-Type':'application/json'
      'Authentication' : 'Token'}
    try:
        r = req.post(url, data=json.dumps(payload), headers=headers)
    except Timeout:
      pass
    except ConnectionError:
      pass
    return r;

def create(dev):
  result = None
  if dev['type'] in devices.__all__:
    module_ = __import__('devices.' + dev['type'])
    d_mod_ = getattr(module_, dev['type'])
    class_ = getattr(d_mod_, dev['type'].title())
    result = class_(dev)
  return result
