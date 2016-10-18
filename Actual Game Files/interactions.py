import time
import config
import map
import gameparser

global answer1
global answer2
global answer3
global answer4
global answer5
answer1 = "unanswered"
answer2 = "unanswered"
answer3 = "unanswered"
answer4 = "unanswered"
answer5 = "unanswered"
def console():
	global answer1
	global answer2
	global answer3
	global answer4
	global answer5
	print("\nHello subject. The questions are:\n1) What is your name?\n2) Who created this facility?\n3) What is your purpose?\n4) What is the name of the company operating this facility?\n5) What are you?\n\nAre you ready to answer a question?")
	print("YES")
	print("NO")
	print("VIEW answers")
	print("CLEAR answers")
	print("SUBMIT answers, this can only be done once.")
	choice = input()
	if choice == "yes":
		print("Please select a question to answer, 1/2/3/4/5:")
		question = input()
		if question == "1":
			if answer1 == "unanswered":
				print("What is your name?")
				answer1 = input()
			else:
				print("Do you want to overwrite your previous answer:")
				print(answer1)
				if input("YES\nNO\n") == "yes":
					print("What is your name?")
					answer1 = input()
		if question == "2":
			if answer2 == "unanswered":
				print("Who created this facility?")
				answer2 = input()
			else:
				print("Do you want to overwrite your previous answer:")
				print(answer2)
				if input("YES\nNO\n") == "yes":
					print("Who created this facility?")
					answer2 = input()
		if question == "3":
			if answer3 == "unanswered":
				print("What is your purpose?")
				answer3 = input()
			else:
				print("Do you want to overwrite your previous answer:")
				print(answer3)
				if input("YES\nNO\n") == "yes":
					print("What is your purpose?")
					answer3 = input()
		if question == "4":
			if answer4 == "unanswered":
				print("What is the name of the company operating this facility?")
				answer4 = input()
			else:
				print("Do you want to overwrite your previous answer:")
				print(answer4)
				if input("YES\nNO\n") == "yes":
					print("What is the name of the company operating this facility?")
					answer4 = input()
		if question == "5":
			if answer5 == "unanswered":
				print("What are you?")
				answer5 = input()
			else:
				print("Do you want to overwrite your previous answer:")
				print(answer5)
				if input("YES\nNO\n") == "yes":
					print("What are you?")
					answer5 = input()
		print("Returning you to menu...")
		time.sleep(1.4)
		console()
	elif choice == "view":
		print("Here are your current answers:")
		print("1) What is your name?\n"+answer1+"\n2) Who created this facility?\n"+answer2+"\n3) What is your purpose?\n"+answer3+"\n4) What is the name of the company operating this facility?\n"+answer4+"\n5) What are you?\n"+answer5)
		time.sleep(3)
		console()
	elif choice == "clear":
		if input("Are you sure you want to clear all of your current answers?\nYES\nNO\n") == "yes":
			answer1,answer2,answer3,answer4,answer5 = "unanswered"
			print("Answers cleared.")
			time.sleep(2)
			console()
	elif choice == "no":
		print("Very well. Explore the complex and find the answers. Quickly now.")
	elif choice == "submit":
		if input("Are you sure you want to submit your answers?\nYES\nNO\n") == "yes":
			print("Excellent. Assessing your performance....")
			score = 0
			if "harris" in gameparser.normalise_input(str(answer1)):
				score = score+1
			if "esther" in gameparser.normalise_input(str(answer2)):
				score = score+1
			if "jakobe" in gameparser.normalise_input(answer2):
				score = score + 1
			if "franco" in gameparser.normalise_input(answer2):
				score = score + 1
			if "freedom" in gameparser.normalise_input(answer3):
				score = score+1
			if "culture" in gameparser.normalise_input(answer4):
				score = score+1
			if "complex" in gameparser.normalise_input(answer4):
				score = score+1
			if "human" in gameparser.normalise_input(answer5):
				score = score+1
			config.won = True
			config.score = score
			return
	else:
		print("Command not recognised.")
		console()

interact_console = {
	"id": "console",
	"name":"the console in the centre of the room",
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
	print('BB-8 beeps friendly. He displays a hint from Jedi Master Luke Skywalker \n- Look at your hands to dermine your cognitive abilities.')

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
	item_records = {
    'id':'records',
    'name': 'an experiment record page',
    'description': 'You read: \nNAME: Harris \nNUMBER: 983762 \nSTATUS: Experiment interrupted.'}
	print("You open the crates, revealing their contents; an experiment record page.")
	map.room_indiana["items"].append(item_records)

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
	print('''This is an emergency broadcast. Culture Complex's servers are down. \nDo not attempt to interact with any artificial beings. \nThis is vital for your safety. \nThis broadcast will repeat in thirty seconds.''')

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
	print('You look at your reflection in the mirror: \nDark hair, blue eyes, athletic physique. You are handsome.\nYou are wearing a hospital gown with a number on it - 983762.\nYou take a closer look at your hand.\nMovement of your muscles allows your palm to be stretched and compressed.\nYou can feel the blood flowing in your veins.\nYou"'" pretty sure that you are human.")

interact_mirror = {
	'id': 'mirror',
	'name': 'a mirror',
	'action': mirror
}

def book():
	print('''You open the book titled 'Culture Complex's social experiment records'. \nIt includes lists of hundreds of names, numbers, dates and room names.''')

interact_book = {
	'id': 'book', 
	'name': 'a book',
	'action': book
}