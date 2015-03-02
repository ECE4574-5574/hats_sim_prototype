"""
    House object : Contains list of global parameters
"""

class House:
    def __init__(self):
        self.rooms = []
        self.connectivity_status = ""
        self.system_time = ""

    #Getters
    def get_rooms(self):
        return self.rooms

    def get_connectivity_status(self):
        return self.connectivity_status


    def get_system_time(self):
        return self.system_time

    #Setters
    def add_room(self, room_object):
        self.rooms.append(room_object)

    def set_connectivity_status(self,connectivity_status):
        self.connectivity_status = connectivity_status

    def set_system_time(self, system_time):
        self.system_time = system_time

