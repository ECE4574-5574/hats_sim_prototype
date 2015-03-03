"""
    House object : Contains list of global parameters
"""
import networkx as nx
from room import Room, Door
from hats_sim import device_hub_server as dhs

class House(nx.Graph):
  def __init__(self, cfg):
    super(House, self).__init__()
    self.connectivity_status = cfg.get('connected', True)
    self.hub = dhs.DeviceHubRequestServer(('',8080), dhs.DeviceHubRequestHandler)
    self.thread = dhs.serveInBackground(self.hub)

  def stop(self):
    self.hub.shouldStop = True
    self.thread.join(30)

  def register_device(self, room, d_name, dev):
    self.hub.add_device("/devices/" + d_name, dev)

  def get_room(self, name):
    return self.node[name]['data']

  def move_user(self, user_id, source, target):
    """Attempts to move a user from one room to an adjacent one"""
    result = False
    try:
        if not self[source][target]['data'].locked():
            curr_room = self.get_room(source)
            next_room = self.get_room(target)
            user = curr_room.get_user(user_id)
            curr_room.rm_user(user_id)
            next_room.add_user(user_id, user)
            result = True
            print 'Moved to ', target
    except KeyError:
        print 'Cannot find ', target
        pass
    return result

  def connectivity_status(self):
    return self.connectivity_status

  def set_connectivity_status(self, connectivity_status):
    self.connectivity_status = connectivity_status
