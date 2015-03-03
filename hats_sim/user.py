class User:
  def __init__(self, cfg = {}):
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