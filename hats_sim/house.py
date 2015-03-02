"""
    House object : Contains list of global parameters
"""
import networkx as nx
from room import Room, Door

class House(nx.Graph):
  def __init__(self):
    super(House, self).__init__()
    self.connectivity_status = True

  def move_user(self, user_id, source, target):
    """Attempts to move a user from one room to an adjacent one"""
    result = False
    try:
        if not self[source][target]['data'].locked():
            user = graph.node[source]['data'].get_user(user_id)
            graph.node[source].rm_user(user_id)
            graph.node[target].add_user(user_id, user)
            result = True
    except KeyError:
        pass
    return result

  def connectivity_status(self):
    return self.connectivity_status

  def set_connectivity_status(self, connectivity_status):
    self.connectivity_status = connectivity_status
