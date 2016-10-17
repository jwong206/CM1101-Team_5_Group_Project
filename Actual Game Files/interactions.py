import time
import config

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

interact_console = {"id": "console","name":"the console in the middle of the room","action":console}

def arcade():
	print("You approach the machine and it turns on, practically inviting you to play.\nYou grab the joystick and start tapping buttons until you get a new highscore!\nThe leaderboard proudly displays the score, and next to it you notice a name: Harris")

interact_arcade = {"id": "arcade","name":"the classic arcade game","action":arcade}