#Module for things used multiple times throughout the program
from items import *
won = False
score = 0
import time

def execute_note():
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    notes = item_notepad["description"]
    print(notes)
    item_notepad["description"] = notes + "\n" + input("What would you like to add to your notepad?\n") + "\n"
    print('\nAdded to notepad.')
    time.sleep(1)