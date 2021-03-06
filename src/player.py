# Write a class to hold player information, e.g. what room they are in
# currently.

# Player Class
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self, name, current_room):
        print(f"Hello {self.name}! You are {self.current_room}.")
