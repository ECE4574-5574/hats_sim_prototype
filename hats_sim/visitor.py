# Visitor Base Class for iterating over graphs
# Author: Jason Ziglar <jpz@vt.edu>

from house import House
import requests as req
import json

class Visitor:
  def traverse_start(self, graph):
    """Signature of function called at the start of each traversal"""
    raise NotImplementedError

  def traverse_end(self, graph):
    """Signature of function called at the end of each traversal.

    The return value of this function will be returned from traverse_all.
    """
    raise NotImplementedError

  def process_room(self, graph, node):
    """Signature called for each room in the graph.

    node -- the identifier of the node currently under consideration
    self.process_users(node) still needs clarification for implementation
    """
    raise NotImplementedError

  def process_door(self, graph, source, target):
    """Signature called for each edge in graph.

    source -- starting location of the edge
    target -- ending location of the edge
    """
    raise NotImplementedError

  def traverse_all(self, graph):
    """Traverse over entire graph, processing every element"""
    self.traverse_start(graph)
    for node in graph.nodes_iter():
      self.process_room(graph, node)
    for edge in graph.edges_iter():
      self.process_door(graph, edge[0], edge[1])
    return self.traverse_end(graph)
