#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from interactions import *
from gameparser import *
import config
import time
import sys
import datetime
from datetime import datetime
global introcount
inv = []

def introanimation():
    config.won = False
    global introcount
    intro = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghx"
    for char in intro:
        introcount = introcount - 1
        time.sleep(0.01)
        if introcount == 0:
            print("Loading complete.\n\n")
            time.sleep(1)
            print_by_char("Welcome.",0.02)
            time.sleep(1.5)
            title()
            break
        time.sleep(0.006)
        if char is "a":
            print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "b":
            print(" \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "c":
            print("  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "d":
            print("   \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "e":
            print("   ////////////////////////////////////////")
        time.sleep(0.006)
        if char is "f":
            print("  ////////////////////////////////////////")
        time.sleep(0.006)
        if char is "g":
            print(" ////////////////////////////////////////")
        time.sleep(0.006)
        if char is "h":
            print("////////////////////////////////////////")
        time.sleep(0.006)
        if char is "x":
            print("Loading...")
            time.sleep(0.01)
            introanimation()

def title():
    print("\n" * 15)
    print("--------------------------------------------------------------------------------------------------------")
    time.sleep(0.02)
    print("   |             /                                  |                                  \             |")
    time.sleep(0.02)
    print("   |            /                                   |                                   \            |")
    time.sleep(0.02)
    print("   |           /                                    |                                    \           |")
    time.sleep(0.02)
    print("   |          /                                    /|\                                    \          |")
    time.sleep(0.02)
    print("   |         /                                     |||                                     \         |")
    time.sleep(0.02)
    print("   |        /                                     / | \                                     \        |")
    time.sleep(0.02)
    print("   |       /                                     /  |  \                                     \       |")
    time.sleep(0.02)
    print("   |      /                                      |  |  |                                      \      |")
    time.sleep(0.02)
    print("   |     /                                       |  |  |                                       \     |")
    time.sleep(0.02)
    print("   |    /                                        |  |  |                                        \    |")
    time.sleep(0.02)
    print("   |   /                                        /   |   \                                        \   |")
    time.sleep(0.02)
    print("   |  /                                         |   |   |                                         \  |")
    time.sleep(0.02)
    print("   | /                                         /    |    \                                         \ |")
    time.sleep(0.02)
    print("   |/                     ▄████████            |    |    |            ▄███████▄                     \|")
    time.sleep(0.02)
    print("   |                     ███    ███            |    |    |            ███    ███                     |")
    time.sleep(0.02)
    print("   |                     ███    █▀             |    |    |            ███    ███                     |")
    time.sleep(0.02)
    print("   |                     ███                  /     |     \           ███    ███                     |")
    time.sleep(0.02)
    print("   |                    ▀███████████          |     |     |          ▀█████████▀                     |")
    time.sleep(0.02)
    print("   |                             ███         /      |      \          ███                            |")
    time.sleep(0.02)
    print("   |                       ▄█    ███        /       |       \         ███                            |")
    time.sleep(0.02)
    print("   |                      ▄████████▀        █████████████████        ▄████▀                          |")
    time.sleep(0.02)
    print("   |                                        ▀███████████████▀                                        |")
    time.sleep(0.02)
    print("   |                                         ▀█████████████▀                                         |")
    time.sleep(0.02)
    print("   |                                 ___▄▄    \     |     /    ▄▄___                                 |")
    time.sleep(0.02)
    print("   |                         ______%@   ███▄   \----|----/   ▄███   @%______                         |")
    time.sleep(0.02)
    print("   |                 ______.@#          █████\   \  |  /   /█████          #@.______                 |")
    time.sleep(0.02)
    print("   |           _____%@                  █████ \__ \ | / __/ █████                  @%______          |")
    time.sleep(0.02)
    print("   |    ____.@(                         █████    \  |  /    █████                         (@.____    |")
    time.sleep(0.02)
    print("   |---%@-------------------------------█████------#|#------█████-------------------------------@%---|")
    time.sleep(0.02)
    print("   |    ¯¯¯¯¯¯\@,______                 █████  __// | \\\__  █████                 ______,@/¯¯¯¯¯¯    |")
    time.sleep(0.02)
    print("   |                  %&______          █████ /  /  |  \  \ █████          ______&%                  |")
    time.sleep(0.02)
    print("   |                         *@,______  ████▀  /    |    \  ▀████   _____,@*                         |")
    time.sleep(0.02)
    print("   |                                 #@_██▀   /     |     \   ▀██__@#                                |")
    time.sleep(0.02)
    print("   |                                         ▄█████████████▄                                         |")
    time.sleep(0.02)
    print("   |                                        ▄███████████████▄                                        |")
    time.sleep(0.02)
    print("   |                                        █████████████████                                        |")
    time.sleep(0.02)
    print("   |                      ▄██████▄          \       |       /         ▄█   ▄█▄                       |")
    time.sleep(0.02)
    print("   |                     ███    ███          \      |      /         ███ ▄███▀                       |")
    time.sleep(0.02)
    print("   |                     ███    ███           |     |     |          ███ ██▀                         |")
    time.sleep(0.02)
    print("   |                     ███    ███           \     |     /         ▄█████▀                          |")
    time.sleep(0.02)
    print("   |                     ███    ███           |     |     |        ▀▀█████▄                          |")
    time.sleep(0.02)
    print("   |                     ███    ███            \    |    /            ███ ██▄                        |")
    time.sleep(0.02)
    print("   |                     ███    ███            |    |    |            ███ ▀███                       |")
    time.sleep(0.02)
    print("   |\                     ▀██████▀             |    |    |            ███   ▀█▀                     /|")
    time.sleep(0.02)
    print("   | \                                         |    |    |            ▀                            / |")
    time.sleep(0.02)
    print("   |  \                                        \    |    /                                        /  |")
    time.sleep(0.02)
    print("   |   \                                        |   |   |                                        /   |")
    time.sleep(0.02)
    print("   |    \                                       |   |   |                                       /    |")
    time.sleep(0.02)
    print("   |     \                                      |   |   |                                      /     |")
    time.sleep(0.02)
    print("   |      \                                     \   |   /                                     /      |")
    time.sleep(0.02)
    print("   |       \                                     |  |  |                                     /       |")
    time.sleep(0.02)
    print("   |        \                                    \  |  /                                    /        |")
    time.sleep(0.02)
    print("   |         \                                    | | |                                    /         |")
    time.sleep(0.02)
    print("   |          \                                   \ | /                                   /          |")
    time.sleep(0.02)
    print("   |           \                                   |||                                   /           |")
    time.sleep(0.02)
    print("   |            \                                   |                                   /            |")
    time.sleep(0.02)
    print("   |             \                                  |                                  /             |")
    time.sleep(0.02)
    print("---|-------------------------------------------------------------------------------------------------|---")
    main_menu()

def main_menu():

    print("\n                      Welcome to SPOK. Please select an option by typing it below.\n\n                                  -NEW GAME- || -CREDITS- || -QUIT- \n")

    selection = normalise_input(input('> '))

    if type(selection) == list:
        if "new" in selection:
            print("Starting new game...")
            time.sleep(1)
            print("\n" * 72)
            main()
        elif "credits" in selection:
            print()
            print_by_char("A game by Team 5.\n\n", 0.02)
            time.sleep(0.5)
            print_by_char("Charlie Bennet\nKonstancja Andrzejewska\nWill Sambells\nJoshua Wong\nMark thomlinson\nCiara Swift\nKieran Fewell\n", 0.02)
            time.sleep(0.5)
            print_by_char("Honorable Mention:\nRobin Watson\n", 0.02)
            time.sleep(0.5)
            print_by_char("We hope you enjoy our game!\n", 0.02)
            time.sleep(2)
            main_menu()
        elif "quit" in selection:
            print("Quitting so soon? We don't think so.")
            main_menu()
        else:
            print("Cooperate.\n")
            time.sleep(1)
            main_menu()

def list_of_items(items):

    itemlist = ""
    for i in items:
        itemlist = itemlist + i["name"] + ", "
    itemlist = itemlist[:len(itemlist)-2]
    return itemlist


def print_room_items(room):

    itemlist =" There is " + list_of_items(room["items"]) + " here.\n"
    if itemlist != " There is " + " here.\n":
        print(itemlist)

def print_room_interacts(room):

    interact_list =" You can interact with " + list_of_items(room["interacts"]) + " here.\n"
    if interact_list != " You can interact with "+" here.\n":
        print(interact_list)


def print_inventory_items(items):

    print("You have " + list_of_items(items) +".\n")


def print_room(room):

    # Display room name
    print("\n\n\n---------------------------\n\n\n")

    print_by_char("TIME: "+ str(datetime.now().time())[:8],0.04)
    time.sleep(0.5)
    print_by_char("DATE: "+room["date"],0.04)
    time.sleep(0.5)
    print_by_char("LOCATION: "+room["name"].upper(),0.04)
    time.sleep(0.7)
    # Display room description
    print(room["description"])


def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):

    print(" GO " + direction.upper() + " to " + leads_to + ".")


def print_search(room_items, room_interacts):

    if print_room_items(current_room) != None:
        print(print_room_items(current_room))
        print()
    if print_room_interacts(current_room) != None:
        print(print_room_interacts(current_room))
        print()
    elif current_room["items"] == [] and current_room["interacts"] == []:
        print("There is nothing here.")
        print()
    print('You can:')
    for i in room_items:
        print(" TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    for i in room_interacts:
        print(" INTERACT " + i["id"].upper() + " to interact with " + i["name"] + ".")
    print(" NOTE to add to your notepad.")
    print(" RETURN to stop searching the room.")


def print_inventory(inventory):
    for i in inventory:
        if i != item_notepad:
            print(" DROP " + i["id"].upper() + " to drop " + i["name"] + ".")
    for i in inventory:
        print(" EXAMINE " + i["id"].upper() + " to examine " + i["name"] + ".")
    print(" NOTE to add to your notepad.")
    print(" RETURN to close your inventory.")


def print_menu(exits, inv_items):

    print("You can type:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    print(" INVENTORY to open your inventory.")
    print(' SEARCH to search ' + current_room['name'] + '.')
    print(" NOTE to add to your notepad.")

    print("\nWhat do you want to do?")


def is_valid_exit(exits, chosen_exit):

    return chosen_exit in exits


def execute_go(direction):

    global current_room
    if is_valid_exit(current_room["exits"],direction) == True:
        current_room = move(current_room["exits"],direction)
        print(('\nGoing ' + str(direction)) + '...')
        time.sleep(1)
    else:
        print ("You cannot go there.")
        time.sleep(1.5)


def execute_search():

    print("\n\n\n---------------------------\n\n\n")

    print('You searched the room...\n')
    print_search(current_room['items'], current_room['interacts'])
    print('\nWhat do you want to do?')
    print()
    command = normalise_input(input('> '))
    if type(command) == list:
        if command[0] == "take":
            if len(command) > 1:
                execute_take(command[1])
                execute_search()
                time.sleep(0.8)
            else:
                print("Take what?")
                time.sleep(0.8)
                execute_search()
        elif command[0] == 'interact':
            if len(command) > 1:
                execute_interact(command[1])
                execute_search()
            else:
                print("Interact with what?")
                time.sleep(0.8)
                execute_search()
        elif command[0] == 'return':
            print("\nReturning to room...")
            time.sleep(0.8)
        elif command[0] == "note":
            config.execute_note()
            execute_search()
        else:
            print("That doesn't make sense.")
            execute_search()
    elif command == None:
        execute_search()


def execute_inventory():

    print("\n\n\n---------------------------\n\n\n")

    print_inventory_items(inventory)
    print('You can:')
    print_inventory(inventory)
    print('\nWhat do you want to do?')
    print()
    command = normalise_input(input('> '))
    if type(command) == list:
        if command[0] == "drop":
            if len(command) > 1:
                execute_drop(command[1])
                execute_inventory()
            else:
                print("Drop what?")
                time.sleep(0.8)
                execute_inventory()
        elif command[0] == 'examine':
            if len(command) > 1:
                execute_examine(command[1])
                execute_inventory()
            else:
                print('Examine what?')
                time.sleep(0.8)
                execute_inventory()
        elif command[0] == 'return':
            print("\nReturning to room...")
            time.sleep(0.8)
        elif command[0] == "note":
            config.execute_note()
            execute_inventory()
        else:
            print("That doesn't make sense.")
            execute_inventory()
    elif command == None:
        execute_inventory()


def execute_take(item_id):

    takeable = False
    for i in current_room["items"]:
        if i["id"] == item_id:
            takeable = True
            inventory.append(i)
            current_room["items"].remove(i)
            print("You have taken " + i['name'] + ".")
            time.sleep(1.2)
    if takeable == False:
        print("You cannot take that.")
        time.sleep(1.5)


def execute_drop(item_id):

    droppable = False
    for i in inventory:
        if i["id"] == item_id:
            droppable = True
            inventory.remove(i)
            current_room["items"].append(i)
            print("You have dropped the " + i['id'] + ".")
            time.sleep(1.2)
    if droppable == False:
        print("You cannot drop that.")
        time.sleep(1.5)


def execute_examine(item_id):
    examinable = False
    for i in inventory:
        if i['id'] == item_id:
            examinable = True
            print()
            print(i['description'])
            # Added varying wait time for reading item description
            if len((i['description'].split())) >= 20:
                time.sleep(8)
            elif len((i['description'].split())) >= 10:
                time.sleep(4)
            else:
                time.sleep(2)
    if examinable == False:
        print('You cannot examine that.')
        time.sleep(1.5)


def execute_interact(interact_id):
	interactable = False
	for i in current_room["interacts"]:
		if i['id'] == interact_id:
			interactable = True
			print("\n")
			i['action']()
			time.sleep(2)
	if interactable == False:
		print('You cannot interact with that.')
		time.sleep(1.5)


def execute_command(command):

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
            time.sleep(0.8)

    elif command[0] == 'search':
    		execute_search()

    elif command[0] == 'inventory':
            execute_inventory()

    elif command[0] == 'note':
    		config.execute_note()
    else:
        print("This makes no sense.")
        time.sleep(0.8)


def menu(exits, inv_items):
    # Display menu
    print_menu(exits, inv_items)

    # Read player's input
    user_input = input('> ')

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    if normalised_user_input != None:
        return normalised_user_input
    else:
        return "invalid"

def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    global command
    # Main game loop
    while config.won == False:
        # Display game status (room description, inventory etc.)
        config.searched = False
        print_room(current_room)
        command = menu(current_room["exits"], inventory)
        execute_command(command)

def print_by_char(string,wait):
	for char in string:
		sys.stdout.write( '%s' % char )
		sys.stdout.flush()
		time.sleep(wait)
	print()


introcount = 20
print_by_char("Initialising...",0.01)
time.sleep(0.5)
print_by_char("Loading...",0.02)
time.sleep(1.2)
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    introanimation()
