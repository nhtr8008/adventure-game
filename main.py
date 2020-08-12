import json
from room import Room

# Global Variable to make sure game is running
is_game_running = True

# Setup function for game to configure rooms
def load_game():
    rooms = {} # empty dictionary
    with open('./config.json') as f:
        data = json.load(f)
    
    # Parse through file and create map of Rooms
    for room in data['Rooms']:
        # create Room object
        new_room = Room(room['id'], room['name'], room['description'], json.loads(room['item']))
        rooms[room['id']] = new_room # put object in dictionary to access it later with room_id

    # Add all the connections between rooms
    for room_id in rooms.keys():
        # Get the connected rooms from the config file. Since the room_id is the
        # same as the element in the Rooms array, we can access using the key
        connected_rooms = data['Rooms'][room_id]['connected_rooms']
        for direction in connected_rooms.keys():
            rooms[room_id].connect_room(rooms[connected_rooms[direction]], direction)
    
    return rooms

if __name__ == '__main__':
    rooms = load_game()
    current_room = rooms[0]
    while is_game_running:		
        print("\n")         
        current_room.look()         
        command = input("> ") 
        if command == "look":
            current_room.look()
        elif command == "quit":
            is_game_running = False
            print("Goodbye!")
        else:
            current_room = current_room.move(command)
            is_game_running = current_room.check_item()
        