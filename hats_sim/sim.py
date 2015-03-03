#!/usr/bin/env python
# Basic Simulator Design
# Author: Jason Ziglar <jpz@vt.edu>

import argparse
import networkx as nx
from convert_visitor import ConvertVisitor
from sim_visitor import SimVisitor
import matplotlib.pyplot as plt
import os

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

if __name__ == "__main__":
  #Run simulator here
  parser = argparse.ArgumentParser(description='Simulator for the HATS home automation system.')
  parser.add_argument('config', help="YAML configuration file")
  parser.add_argument('--house', help="File specifying the house to load.")
  args = parser.parse_args()

  try:
    with open(args.config, 'r') as f:
      config = load(f, Loader=Loader)
  except:
    config = {}

  if 'house' in args and args.house is not None:
    config['house'] = args.house
  fname, ext = os.path.splitext(config['house'])

  convert = False
  if ext == '.pickle':
    house = nx.read_gpickle(config['house'])
  elif ext == '.yaml':
    try:
      with open(config['house'], 'r') as f:
        house_cfg = load(f, Loader=Loader)
    except:
      house_cfg = {}
    path = os.path.join(os.path.dirname(__file__), '..', 'houses', house_cfg['graph'])
    base_graph = nx.read_graphml(path)
    convert = True
  else:
    raise SystemError(args.house + " is not of a known supported format!")

  if convert:
    convert = ConvertVisitor(house_cfg)
    house = convert.traverse_all(base_graph)

  if config.get('show_graph', True):
    plt.ion()
    nx.draw_networkx(house, with_labels=True)
    plt.draw()
  sim_update = SimVisitor(config['sim'])
  try:
    # Loop here
    while True:
      sim_update.traverse_all(house)
  except KeyboardInterrupt:
    house.stop()
    if 'save_house' in config:
      nx.write_gpickle(house, config['save_house'])
