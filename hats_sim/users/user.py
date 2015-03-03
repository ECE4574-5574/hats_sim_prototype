#!/usr/env python
# Author: Jason Ziglar <jpz@vt.edu>

import users

class User(object):
  def __init__(self, name, cfg = {}):
    self.name = name

  def visit(self, graph, node, time):
    pass

def create(name, cfg):
  """Creates a user based on the configuration provided"""
  result = None
  if cfg['type'] in users.__all__:
    module_ = __import__('users.' + cfg['type'])
    d_mod_ = getattr(module_, cfg['type'])
    instance = cfg.get('instance', cfg['type']).title()
    class_ = getattr(d_mod_, instance)
    result = class_(name, cfg)
  return result