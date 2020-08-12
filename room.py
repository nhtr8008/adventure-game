class Room():
    def __init__(self, id, name, description, is_item):
        self.id = id
        self.name = name
        self.description = description
        self.connected_rooms = {} # dictionary for connected rooms. empty because not built yet.
        self.is_item = is_item

    def connect_room(self, room_to_connect, direction):
        self.connected_rooms[direction] = room_to_connect

    def check_item(self):
        if self.is_item:
            print("You have the key to escape!")
            return False
        else:
            return True

    def look(self):
        # print details of room if user enters look command
        print(self.description)
        for direction in self.connected_rooms: #this for loop iterates through the dictionary and printing out the connections each room has
            room = self.connected_rooms[direction] #getting room in that direction
            print( "The " + room.name + " is " + direction)

    # method to allow player to move between rooms.
    def move(self, direction):
        if direction in self.connected_rooms:
            return self.connected_rooms[direction]
        else:
            print("Unable to move that direction.")
            return self
