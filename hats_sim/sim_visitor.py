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
    self.cycle_rate = config.get('cycle_rate', 10.0)
    self.last_time = self.start_time
  def traverse_start(self, graph):
    """Computes time step for this traversal."""
    self.step_start = time.time()
    # print now, self.last_time
    time_step = 1.0 / self.cycle_rate
    self.time =  (time_step * self.time_scale) + self.last_time
    self.step_end = self.step_start + time_step
  def traverse_end(self, graph):
    """Preps for next time step computation."""
    now = time.time()
    diff = self.step_end - now
    if diff > 0.0:
      time.sleep(diff)
    self.last_time = self.step_start
  def process_room(self, graph, node):
    """Call visit on the room defined in data."""
    graph.node[node]['data'].visit(graph, node, self.time)
  def process_door(self, graph, source, target):
    """Call visit on the door defined in data."""
    graph[source][target]['data'].visit(graph, source, target, self.time)