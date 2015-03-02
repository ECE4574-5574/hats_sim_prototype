from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import logging
import threading
import time
from simulated_devices import HatsSimDevice, LightSwitch, Thermostat

#Contains classes and functions for simulating a device hub by providing a server that responds to HTTP requests.
#Basic use pattern: Construct a DeviceHubRequestServer. Pass it to serveInBackground(). The returned thread
#will run until the server is sent an HTTP QUIT. You should wait until the thread is done before allowing any application
#using this class to terminate.

#Running this file from the command line will start a server listening on this port (as a demo):
LISTEN_PORT = 8080

#This implementation of an HTTP server is based on Python's built-in BaseHTTPServer.
#Each time the server handles a request, it instantiates one of these objects.
#The object has member fields that contain information about the request it is meant to service, and a pointer
#to the server object that created it.
#The do_VERB() function is called for each HTTP verb.
class DeviceHubRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.server.devicesLock.acquire()
		try:
			if self.path in self.server.devices:
				self.send_response(200)
			else:
				self.send_response(404)
			self.end_headers()
		finally:
			self.server.devicesLock.release()
	
	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		self.server.logger.debug('I\'m pretending to handle a POST...')
		return

	def do_QUIT(self):
		self.send_response(200)
		self.end_headers()
		self.server.shouldStop = True
		
#An extension of HTTPServer. Has a dictionary of devices keyed to their IDs (which become paths)
class DeviceHubRequestServer(HTTPServer):

	def __init__ (self, server_address, RequestHandlerClass):
		HTTPServer.__init__(self, server_address, RequestHandlerClass)
		self.logger = logging.getLogger('DeviceHubRequestServer')
		self.shouldStop = False
		self.devices = {}
		self.devicesLock = threading.Lock()

	def serve_forever (self):
		while not self.shouldStop:
			self.handle_request()

	def add_device (self, device):
		self.devicesLock.acquire()		
		try:
			self.devices[device.deviceID] = device
		finally:
			self.devicesLock.release()

	def get_device (self, deviceID):
		self.devicesLock.acquire()
		try:
			if deviceID in self.devices:
				return self.devices[deviceID]
			else:
				return None
		finally:
			self.devicesLock.release()

def runServer(server):
	server.serve_forever()

def serveInBackground(server):
	thread = threading.Thread(target=runServer, args=(server,))
	thread.start()
	return thread

if __name__ == "__main__":
	logging.basicConfig(format='%(asctime)s %(message)s')
	server=DeviceHubRequestServer(('',LISTEN_PORT), DeviceHubRequestHandler)
	atriumlight = LightSwitch('/user/home/devices/atrium/lightswitch', False)
	kitchenlight = LightSwitch('/user/home/devices/kitchen/lightswitch', False)
	server.add_device(atriumlight)
	server.add_device(kitchenlight)
	server.logger.setLevel(logging.DEBUG)
	serverThread = serveInBackground(server)
	try:
		while serverThread.isAlive():
			print 'Serving...'
			time.sleep(10)
			print 'Still serving...'
			time.sleep(10)
	except KeyboardInterrupt:
		pass

