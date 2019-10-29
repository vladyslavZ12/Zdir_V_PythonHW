#import the randop package so that we can generate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

#set the computer variable to one of these choices (0,1or2)
computer=choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False

while player is False:
    #se player to true
    print("*********************************\n\n")
    print("choose your weapon!\n\n")
    print("*********************************\n\n")
    
    player = input("choose rock, paper or scissors\n\n")

    print("computer chose ", computer, "\n")
    print("player choose ", player, "\n")

    if computer == player:
	    print ("tie! no one wins, play again")
    elif player.lower() =="quit":
        exit()
    elif player.lower() == "rock":
        if computer == "paper":
            print("you lose!", computer, "covers", player,"\n")
        else:
        	print("you win!", player, "smashes through", computer, "\n")
    elif player.lower() == "paper":
        if computer == "scissors":
            print("you lose!", computer, "cuts", player,"\n")
        else:
        	print("you win!", player, "coveres", computer, "\n")
    elif player.lower() == "scissors":
        if computer == "rock":
            print("you lose!", computer, "smashes", player,"\n")
        else:
        	print("you win!", player, "cuts", computer, "\n")
    else:
    	print("that's not a valid choice, try again")

    # need to check all of our conditions after checking for a tie

    player = False
    computer = choices[randint(0, 2)]