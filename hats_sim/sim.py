#!/usr/bin/env python
# Basic Simulator Design
# Author: Jason Ziglar <jpz@vt.edu>

import argparse
import networkx as nx
from convert_visitor import ConvertVisitor
from sim_visitor import SimVisitor
import matplotlib.pyplot as plt

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

if __name__ == "__main__":
  #Run simulator here
  parser = argparse.ArgumentParser(description='Simulator for the HATS home automation system.')
  parser.add_argument('config')
  args = parser.parse_args()

  with open(args.config, 'r') as f:
    config = load(f, Loader=Loader)

  if 'house_file' in config:
    house = nx.read_gpickle(config['house_file'])
  elif 'house_graph' in config:
    base_graph = nx.read_graphml(config['house_graph'])
    convert = ConvertVisitor()
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
    if 'save_house' in config:
      nx.write_gpickle(house, config['save_house'])