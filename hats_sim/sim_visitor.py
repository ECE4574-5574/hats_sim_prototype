# Visitor which calls update on each object for the simulation.
# Author: Jason Ziglar <jpz@vt.edu>

import networkx as nx
from visitor import Visitor
import time

class SimVisitor(Visitor):
  def __init__(self, config):
    """ Configures visitor for sim time."""
    now = time.time()
    self.start_time = config.get('start_time', now)
    self.time_scale = config.get('time_scale', 1.0)
    self.last_time = self.start_time
  def traverse_start(self, graph):
    """Computes time step for this traversal."""
    self.step_start = time.time()
    # print now, self.last_time
    time_step = (self.step_start - self.last_time)
    self.time =  (time_step * self.time_scale) + self.start_time
  def traverse_end(self, graph):
    """Preps for next time step computation."""
    self.last_time = self.step_start
  def process_room(self, graph, node):
    """Call visit on the room defined in data."""
    graph.node[node]['data'].visit(graph, node, self.time)
  def process_door(self, graph, source, target):
    """Call visit on the door defined in data."""
    graph[source][target]['data'].visit(graph, source, target self.time)