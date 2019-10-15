## Name: Robert Kreml
## Date: October 11, 2019
## Class: EPSY 5200

## Exercise 35 from LP3TH by Zed Shaw


from sys import exit

def gold_room():
	print ("This room is full of gold. How much do you take?")
	print ("Type a number from 0 as the lowest to 100 as the highest.")
	
	next = input("> ")
	if next < 100:
		print ("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You got too greedy and can not carry the heavy gold back out! You died...")

def pool_room():
	print("This room is filled with water. Do you swim across?")

	next = input("> ")
	if next == "yes":
		print("You make it across the pool and can proceed into the gold room!")
		gold_room()
	if next == "no":
		dead("A monster comes up from behind you and you die!")
		
def bear_room():
	print ("There is a bear here.")
	print ("The bear has a bunch of honey.")
	print ("The fat bear is in front of another door.")
	print ("How are you going to move the bear?")
	print ("Your options are either to 'take honey', 'taunt bear', or 'open door'.")
	bear_moved = False
	
	while True:
		next = input("> ")
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print ("The bear has moved from the door. You can go through it now. ")
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			pool_room()
		elif next == "open door" and not bear_moved:
			dead("The bear swipes you with its claw and you die.")
		else:
			print ("I got no idea what that means.")

def cthulhu_room():
	print ("Here you see the great evil Cthulhu.")
	print ("He, it, whatever stares at you and you go insane.")
	print ("Do you flee for your life or eat your head?")
	print ("Please type either 'flee' or 'head'.")
	
	next = input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print (why, "Good job!")
	exit(0)
	
def start():
	print ("You are in a dark room.")
	print ("There is a door to your right and left.")
	print ("Which one do you take?")
	
	next = input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()

## Study Drills
# 1) I do not know exactly how to draw a map in this context, so I will attach an image of my understanding of the flow.
# 2) No mistakes were identified.
# 3) I understand what each of the functions does.
# 4) Added a new room to the proper play flow and I fixed a few of the print instructions.
# 5) If you type say '2' it wont work. I would just put the int() function in as it is already written.


## Mistakes
# 1) No mistakes in this script to my knowledge.