from room import Room
from player import Player
from item import Item

# Declare all the rooms

locations = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

locations['outside'].n_to = locations['foyer']
locations['foyer'].s_to = locations['outside']
locations['foyer'].n_to = locations['overlook']
locations['foyer'].e_to = locations['narrow']
locations['overlook'].s_to = locations['foyer']
locations['narrow'].w_to = locations['foyer']
locations['narrow'].n_to = locations['treasure']
locations['treasure'].s_to = locations['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
my_player = Player(input("What is your name?"), "outside")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



# Move command, will handle actually moving the player
def go(direction):
    """
    X Values:
    0: north
    1: south
    2: east
    3: west
    """

    if hasattr(player.current_room, direction+"_to"):
        player.current_room = getattr(player.current_room, direction+"_to")
    else:
        print("You can't go that way.")


#
def move(my_player):
    # Where are you currently?
    start_space = my_player.current_room
    print(f"You are currently {start_space}.")

    # Where would you like to go?
    direction = input("Which cardinal direction would you like to move in?")

    # Splitting Direction into Letters
    d_list = direction[0].lower().split()

    # Assigning first letter in the list to a variable
    d = d_list[0]

    # If Elif:
    if d == "n":
        print("North")
    elif d == "s":
        print("South")
    elif d == "e":
        print("East")
    elif d == "w":
        print("West")
    else:
        print("That is not a cardinal direction. Please choose: north, south, east or west.")



if __name__ == "__main__":
    print(f"Current Room: {my_player.current_room}")
    print(f"Room Description: {locations.get(my_player.current_room)}")


    print("---")
    move(my_player)
