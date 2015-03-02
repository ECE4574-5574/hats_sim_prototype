from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import logging
import threading
import time
from simulated_devices import HatsSimDevice, LightSwitch, Thermostat

LISTEN_PORT = 8080

class DeviceHubRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path in self.server.devices:
			self.send_response(200)
		else:
			self.send_response(404)
		self.end_headers()
		return
	
	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		self.server.logger.debug('I\'m pretending to handle a POST...')
		return

	def do_QUIT(self):
		self.send_response(200)
		self.end_headers()
		self.server.shouldStop = True
		

class DeviceHubRequestServer(HTTPServer):

	logger = None
	shouldStop = False
	devices = {}
	
	def __init__ (self, server_address, RequestHandlerClass):
		HTTPServer.__init__(self, server_address, RequestHandlerClass)
		self.logger = logging.getLogger('DeviceHubRequestServer')

	def serve_forever (self):
		while not self.shouldStop:
			self.handle_request()

	def add_device (self, device):
		self.devices[device.deviceID] = device

def runServer(server):
	server.serve_forever()

def serveInBackground(server):
	thread = threading.Thread(target=runServer, args=(server,))
	thread.start()

if __name__ == "__main__":
	logging.basicConfig(format='%(asctime)s %(message)s')
	server=DeviceHubRequestServer(('',LISTEN_PORT), DeviceHubRequestHandler)
	atriumlight = LightSwitch('/user/home/devices/atrium/lightswitch', False)
	kitchenlight = LightSwitch('/user/home/devices/kitchen/lightswitch', False)
	server.add_device(atriumlight)
	server.add_device(kitchenlight)
	server.logger.setLevel(logging.DEBUG)
	serveInBackground(server)
	try:
		while True:
			print 'Serving...'
			time.sleep(10)
			print 'Still serving...'
			time.sleep(10)
	except KeyboardInterrupt:
		pass

