"""
    House object : Contains list of global parameters
"""
import networkx as nx
from room import Room, Door

class House(nx.Graph):
  def __init__(self):
    super(House, self).__init__()
    self.connectivity_status = True

  def connectivity_status(self):
    return self.connectivity_status

  def set_connectivity_status(self, connectivity_status):
    self.connectivity_status = connectivity_status
