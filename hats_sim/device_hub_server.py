from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import logging
import threading
import time

LISTEN_PORT = 8080

class DeviceHubRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.server.logger.debug('I\'m pretending to handle a GET...')
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
	
	def __init__ (self, server_address, RequestHandlerClass):
		HTTPServer.__init__(self, server_address, RequestHandlerClass)
		self.logger = logging.getLogger('DeviceHubRequestServer')

	def serve_forever (self):
		while not self.shouldStop:
			self.handle_request()

def runServer():
	logging.basicConfig(format='%(asctime)s %(message)s')
	server=DeviceHubRequestServer(('',LISTEN_PORT), DeviceHubRequestHandler)
	server.logger.setLevel(logging.DEBUG)
	server.serve_forever()

def serveInBackground():
	thread = threading.Thread(target=runServer)
	thread.start()

if __name__ == "__main__":
	serveInBackground()
	try:
		while True:
			print 'Serving...'
			time.sleep(10)
			print 'Still serving...'
			time.sleep(10)
	except KeyboardInterrupt:
		pass

