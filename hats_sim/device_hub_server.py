from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import logging
import threading
import time
import json
from device import Lights, Alarm

#Contains classes and functions for simulating a device hub by providing a server that responds to HTTP requests.
#Basic use pattern: Construct a DeviceHubRequestServer. Pass it to serveInBackground(). The returned thread
#will run until you set server.shouldStop to true. You should wait until the thread is done (call thread.join())
#before allowing any application using this class to terminate.

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
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
				self.wfile.write(self.server.devices[self.path].toJson())
			else:
				self.send_response(404)
				self.end_headers()
		finally:
			self.server.devicesLock.release()

	def do_POST(self):
		self.server.devicesLock.acquire()
		length = int(self.headers.getheader('content-length', 0))
		payload = self.rfile.read(length)
		self.rfile.close()
		try:
			if self.path in self.server.devices:
				newSettings = json.loads(payload)
				self.server.devices[self.path].update(newSettings)
				self.send_response(200)
				self.end_headers()
			else:
				self.send_response(404)
				self.end_headers()
		finally:
			self.server.devicesLock.release()

	def do_QUIT(self):
		self.send_response(200)
		self.end_headers()
		self.server.shouldStop = True

#An extension of HTTPServer. Has a dictionary of devices keyed to their IDs (which become paths)
class DeviceHubRequestServer(HTTPServer):

	def __init__ (self, server_address, RequestHandlerClass, devices = {}):
		HTTPServer.__init__(self, server_address, RequestHandlerClass)
		self.logger = logging.getLogger('DeviceHubRequestServer')
		self.shouldStop = False
		self.devices = devices
		self.timeout = 1
		self.devicesLock = threading.Lock()
		self.pause_lock = threading.Lock()

	def serve_forever (self):
		while not self.shouldStop:
			self.pause_lock.acquire()
			self.handle_request()
			self.pause_lock.release()

	def pause(self):
		self.pause_lock.acquire()
	def unpause(self):
		self.pause_lock.release()

	def add_device (self, deviceID, device):
		self.devicesLock.acquire()
		try:
			self.devices[deviceID] = device
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
	atriumlight = Lights({'status':False, 'brightness':1.0})
	kitchenlight = Lights({'status':False, 'brightness':1.0})
	initDevices = {'/devices/atriumLight':atriumlight, '/devices/kitchenLight':kitchenlight}
	server=DeviceHubRequestServer(('',LISTEN_PORT), DeviceHubRequestHandler, initDevices)
	alarm = Alarm({})
	server.add_device('/devices/alarm', alarm)
	server.logger.setLevel(logging.DEBUG)
	serverThread = serveInBackground(server)
	try:
		while serverThread.isAlive():
			print 'Serving...'
			time.sleep(10)
			print 'Still serving...'
			time.sleep(10)
	except KeyboardInterrupt:
		print 'Attempting to stop server...'
		server.shouldStop = True
		serverThread.join(30)


