#!/usr/env python
# Author: Jason Ziglar <jpz@vt.edu>

from devices import *
from user import User
import random

class Tinker(User):
  def __init__(self, name, cfg):
    super(Tinker, self).__init__(name, cfg)
    self.move_speed = cfg.get('move_speed', 30.0)
    self.tinker_speed = cfg.get('tinker_speed', 10.0)
    self.last_move_time = -1.0
    self.last_tinker_time = -1.0

  def visit(self, graph, node, time):
    if self.last_move_time < 0:
      self.last_move_time = time
    elif time - self.last_move_time > self.move_speed:
      self.move_to_random_room(graph, node)
      self.last_move_time = time

    if self.last_tinker_time < 0:
      self.last_tinker_time = time
    elif time - self.last_tinker_time > self.tinker_speed:
      self.tinker(graph, node)
      self.last_tinker_time = time

  def move_to_random_room(self, graph, node):
    next_room = random.choice(graph.neighbors(node))
    graph.move_user(self.name, node, next_room)

  def tinker(self, graph, node):
    room = graph.get_room(node)
    dev_names = room.device_names()
    if not room.device_names():
        return
    d_name = random.choice(dev_names)
    device = room.get_device(d_name)

    if type(device) is light.Light:
      if device.getBrightness() > 0.5:
        device.turnOff()
      else:
        device.turnOn()