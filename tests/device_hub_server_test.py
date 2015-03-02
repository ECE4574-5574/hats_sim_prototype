#!/usr/bin/env python
# Testing Visitor Pattern over Graphs
# Author: Mark Koninckx <koninckx@vt.edu>
import unittest
import httplib
import logging
import time
from hats_sim import device_hub_server as dhs
from hats_sim import simulated_devices as sd

class DeviceHubServerTest(unittest.TestCase):
	def setUp(self):
		self.server = dhs.DeviceHubRequestServer(('',8080), dhs.DeviceHubRequestHandler)
		self.atriumlight = sd.LightSwitch('/user/home/devices/atrium/lightswitch', False)
		self.kitchenlight = sd.LightSwitch('/user/home/devices/kitchen/lightswitch', False)
		self.server.add_device(self.atriumlight)
		self.server.add_device(self.kitchenlight)
		self.server.logger.setLevel(logging.DEBUG)
		self.thread = dhs.serveInBackground(self.server)

	def testGET(self):
		conn = httplib.HTTPConnection('localhost:8080')
		conn.request('GET', '/user/home/devices/atrium/lightswitch')
		self.assertEqual(conn.getresponse().status, 200)
		conn.request('GET', '/some/path/that/is/nonsense')
		self.assertEqual(conn.getresponse().status, 400)

	def tearDown(self):
		conn = httplib.HTTPConnection('localhost:8080')
		conn.request('QUIT', '')
		self.thread.join(30)

if __name__ == '__main__':
	unittest.main()
