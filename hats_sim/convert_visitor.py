# Visitor which converts a raw graph into a graph full of house objects.
# Useful for reading in graphs from external sources, and adding our framework
# Author: Jason Ziglar <jpz@vt.edu>

import networkx as nx
from visitor import Visitor
from room import Room, Door

class ConvertVisitor(Visitor):
  """Converts a pure graph to a graph with appropriate Python objects.

  This enables converting a function generated in a human readable format
  to be used in the simulation, by decorating nodes and edges with objects.
  """
  def __init__(self):
    pass
  def traverse_start(self, raw_graph):
    """Instantiates a graph to store the house."""
    self.graph = nx.Graph()
  def traverse_end(self, raw_graph):
    """Returns the converted graph."""
    return self.graph
  def process_room(self, raw_graph, node):
    """Adds a room to the graph with the appropriate data."""
    self.graph.add_node(node, data=Room())
  def process_door(self, raw_graph, source, target):
    """Adds an edge to the graph with the appropriate data."""
    self.graph.add_edge(source, target, data=Door())