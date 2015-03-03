# Visitor which converts a raw graph into a graph full of house objects.
# Useful for reading in graphs from external sources, and adding our framework
# Author: Jason Ziglar <jpz@vt.edu>

import networkx as nx
from visitor import Visitor
from house import House
from room import Room, Door
from user import User

class ConvertVisitor(Visitor):
  """Converts a pure graph to a graph with appropriate Python objects.

  This enables converting a function generated in a human readable format
  to be used in the simulation, by decorating nodes and edges with objects.
  """
  def __init__(self, house_cfg):
    self.cfg = house_cfg
  def traverse_start(self, raw_graph):
    """Instantiates a graph to store the house."""
    self.graph = House(self.cfg)
  def traverse_end(self, raw_graph):
    """Returns the converted graph."""
    u_cfg = self.cfg.get('users', {})
    for key, value in u_cfg.items():
      user = User(key, value)
      try:
        self.graph.node[value['location']]['data'].add_user(key, user)
      except KeyError:
        print "%s cannot be created in invalid location" % key
    return self.graph
  def process_room(self, raw_graph, node):
    """Adds a room to the graph with the appropriate data."""
    room_cfg = self.cfg['rooms'].get(node, {})
    room = Room(room_cfg)
    self.graph.add_node(node, data=room)

    for key, value in room.devices_iter():
      self.graph.register_device(node, key, value)
  def process_door(self, raw_graph, source, target):
    """Adds an edge to the graph with the appropriate data."""
    self.graph.add_edge(source, target, data=Door())