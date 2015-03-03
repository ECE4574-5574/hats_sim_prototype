#!/usr/env python

class User:
  def __init__(self, cfg = {}):
    pass
    #self.id = something
    #Set up user configuration here
  def visit(self, graph, node, time):
    # Here is the chance for the user to do something.
    room = graph.node[node]['data']
    # Get list of devices
    nearby_devices = room.get_devices()
    # Attempt to move this user to another room
    success = graph.move_user(self.id, a, b)
    # Do stuff here
    
    	#checks state of random device within room
	def stateChecker():
		# randomly select device from room based on list
		randdev = random.randint(0,len(get_device()); #from room class
		
		currentDev = get_device(randdev);
		devState = currentDev.status;
		devTime = currentDev.time;
		
		if devState == 'true':
			#check device time and if users are in room
			if not getUsers(); #if users list empty in room
				#check device idle time
				if devTime > 360: # seconds to 60 minutes
					currentDev = 'false'
		elif devState == 'sleep':#if there is a mode for continuous run (stay on)
			#continue running current settings regardless of user/idle time
			
		else:

	def moveChecker(); #check if user can move rooms and check statuses
		finding = true;
		randuser = random.randint(0,len(graph.node[node]['data']);  # get random room from list of rooms
		currentRoom = graph.node[randuser]['data']
		success = true
		while success:
			if currentRoom.door == false:
				success = false;	# ends search
				print "Found open room."
			else:
				print "Room ", currentRoom, " ", randuser, " is locked.  Continuing search..."
				randuser += 1;
				if randuser > len(graph.node[node]['data']:
					jumpRoom = graph.node[0]['data']; # start beginning of rooms when it comes to end of list
					success = graph.move_user(self.id, currentRoom, jumpRoom);
				else:
					success = graph.move_user(self.id, currentRoom, graph.node[randuser]['data']);
				
