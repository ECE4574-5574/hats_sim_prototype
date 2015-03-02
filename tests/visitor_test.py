#!/usr/bin/env python
# Testing Visitor Pattern over Graphs
# Author: Jason Ziglar <jpz@vt.edu>
import unittest
import networkx as nx
from hats_sim import visitor, convert_visitor, room

class CountVisitor(visitor.Visitor):
  def traverse_start(self, graph):
    self.node_count = 0
    self.edge_count = 0
  def traverse_end(self, graph):
    return self.node_count, self.edge_count
  def process_room(self, graph, node):
    self.node_count = self.node_count + 1
  def process_door(self, graph, source, target):
    self.edge_count = self.edge_count + 1

class SimpleVisitorTest(unittest.TestCase):
  def setUp(self):
    #Define a simple graph for testing
    self.graph = nx.Graph()
    self.graph.add_node("a")
    self.graph.add_node("b")
    self.graph.add_node("c")
    self.graph.add_node("d")

    self.graph.add_edge("a", "b")
    self.graph.add_edge("c", "d")
    self.graph.add_edge("b", "d")
  def test_visitor(self):
    #Test that the visitor traverses all nodes and edges
    visitor = CountVisitor()
    nodes, edges = visitor.traverse_all(self.graph)
    self.assertEqual(nodes, len(self.graph.nodes()))
    self.assertEqual(edges, len(self.graph.edges()))

    #Second test ensures that we can re-use the visitor without errors
    nodes, edges = visitor.traverse_all(self.graph)
    self.assertEqual(nodes, len(self.graph.nodes()))
    self.assertEqual(edges, len(self.graph.edges()))

    #Test Empty graph
    empty_graph = nx.Graph()
    nodes, edges = visitor.traverse_all(self.graph)
    self.assertEqual(nodes, len(self.graph.nodes()))
    self.assertEqual(edges, len(self.graph.edges()))

  def test_convert_visitor(self):
    visitor = convert_visitor.ConvertVisitor({})
    house = visitor.traverse_all(self.graph)

    #Validate that every node and edge is now given Python classes
    for r_id in house.nodes_iter():
      self.assertTrue(r_id in self.graph.nodes())
      self.assertTrue('data' in house.node[r_id])
      self.assertTrue(isinstance(house.node[r_id]['data'], room.Room))
    for edge in house.edges_iter():
      self.assertTrue(edge in self.graph.edges())
      self.assertTrue('data' in house[edge[0]][edge[1]])
      self.assertTrue(isinstance(house[edge[0]][edge[1]]['data'], room.Door))

if __name__ == '__main__':
  unittest.main()