import time
import config
import map

def win():
	time.sleep(1)
	config.won = True

def console():
	print("Hello subject. The questions are:\n-Who are you?\n-When was Vicky born?\n\nAre you ready to answer?")
	print("Please respond yes/no.")
	if input() == "yes":
		print("Excellent. Please answer the following questions:")
		time.sleep(1)
		print("Who are you?")
		if input() == "Harris":
			print("Good. When was Vicky born? dd/mm/yyyy")
			if input() == "24/05/1819":
				print("Outstanding. You've earned your freedom.")
				win()
			else:
				print("That is not correct.")
		else:
			print("That is not correct.")

	else:
		print("Very well. Explore the complex and find the answers. Quickly now.")

interact_console = {
	"id": "console",
	"name":"the console in the middle of the room",
	"action": console
}

def arcade():
	print("You approach the machine and it turns on, practically inviting you to play.\nYou grab the joystick and start tapping buttons until you get a new highscore!\nThe leaderboard proudly displays the score, and next to it you notice a name: Harris")

interact_arcade = {
	"id": "arcade",
	"name": "the classic arcade game",
	"action": arcade
}

def bb8():
	print('BB-8 beeps friendly. He displays a hint from Jedi Master Luke Skywalker \n- look at your hands to dermine your cognitive abilities.')

interact_bb8 = {
	'id': 'bb8',
	'name': 'a BB-8 droid',
	'action': bb8
}

def holochess():
	print("You fiddle with the holochess, the creatures on the board grumble and roar as they slay eachother.")

interact_holochess = {
	"id": "holochess",
	"name": "the holochess board",
	"action": holochess
}

def tombstone():
	print('You read: PROPERTY OF CULTURE COMPLEX. The rest of the writing is illegible.')

interact_tombstone = {
	'id': 'tombstone',
	'name': 'a tombstone',
	'action': tombstone
}

def crates():
	item_pineapple = {
    'id':'pineapple',
    'name': 'a pineapple',
    'description': 'A placeholder object'}
	print("You open the crates, revealing their contents; a <placeholder pineapple>.")
	map.room_indiana["items"].append(item_pineapple)

interact_crates = {
	"id": "crates",
	"name":"some wooden crates",
	"action":crates
}

def walkietalkie():
	print('Harris, come in. Over.')
	print('Harris, come in. Over.')
	print('Harris, come in. Over.')

interact_walkietalkie = {
	'id': 'walkietalkie',
	'name': 'a walkie-talkie',
	'action': walkietalkie
}

def radio():
	print('This is an emergency broadcast. COMPANY NAME servers are down. \nDo not attempt to interact with any artificial beings. \nThis is vital for your safety. \nThis broadcast will repeat in thirty seconds.')

interact_radio = {
	'id': 'radio',
	'name': 'an emergency radio',
	'action': radio
}

def laptop():
	print('There is a critical batter warining window open: \nYOUR BATTERY IS RUNNING LOW (6%) \n You click OK. There is a BBC website open. The headline reads: \nSCIENTIST COUPLE OPEN AN AMUSMENT PARK WHERE YOU CAN INTERACT WITH ARTIFICAL BEINGS \nJakobe Franco confirms opening date. \nLaptop hibernates. The battery is dead.')

interact_laptop = {
	'id': 'laptop',
	'name': 'a laptop',
	'action': laptop
}

def mirror():
	print('You look at your reflection in the mirror: \nDark hair, blue eyes, athletic physique. You are handsome.\nYou are wearing a hospital gown with a number on it - 983762.\nYou take a closer look at your hand.\nMovement of your muscles allows your palm to be stretched and compressed.\nYou can feel the blood flowing in your veins.')

interact_mirror = {
	'id': 'mirror',
	'name': 'a mirror',
	'action': mirror
}
