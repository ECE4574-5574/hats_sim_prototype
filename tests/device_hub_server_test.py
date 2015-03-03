#!/usr/bin/env python
# Testing Visitor Pattern over Graphs
# Author: Mark Koninckx <koninckx@vt.edu>
import unittest
import httplib
import logging
import time
from hats_sim import device_hub_server as dhs
import hats_sim.devices.light as sd

class DeviceHubServerTest(unittest.TestCase):
	def setUp(self):
		self.server = dhs.DeviceHubRequestServer(('',0), dhs.DeviceHubRequestHandler)
		self.port = self.server.socket.getsockname()[1]
		self.atriumlight = sd.Light({'status':False, 'brightness':1.0})
		self.kitchenlight = sd.Light({'status':False, 'brightness':1.0})
		self.server.add_device('/devices/atriumLight', self.atriumlight)
		self.server.add_device('/devices/kitchenLight', self.kitchenlight)
		self.server.logger.setLevel(logging.DEBUG)
		self.thread = dhs.serveInBackground(self.server)

	def testGetDevice(self):
		self.assertNotEqual(self.server.get_device('/devices/atriumLight'), None)
		self.assertEqual(self.server.get_device('/some/path/that/is/nonsense'), None)

	def testGET(self):
		conn = httplib.HTTPConnection('localhost', self.port)
		conn.request('GET', '/devices/atriumLight')
		resp = conn.getresponse()
		self.assertEqual(resp.status, 200)
		self.assertEqual(resp.read(), self.atriumlight.toJson())
		conn.request('GET', '/some/path/that/is/nonsense')
		self.assertEqual(conn.getresponse().status, 404)

	def tearDown(self):
		conn = httplib.HTTPConnection('localhost', self.port)
		conn.request('QUIT', '')
		self.thread.join(30)

if __name__ == '__main__':
	unittest.main()
