#import the randop package so that we can generate a random choice
from random import randint

# set up some variables for player and AI Lives
player_lives=5
computer_lives=5

# choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

#set the computer variable to one of these choices (0,1or2)
computer=choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False

while player is False:
    #se player to true
    print("*********************************\n")
    print("player lives: ", player_lives, "/5\n")
    print("computer lives: ", computer_lives, "/5\n")
    print("choose your weapon!\n")
    print("*********************************\n")
    
    player = input("choose rock, paper or scissors\n")

    print("computer chose ", computer, "\n")
    print("player choose ", player, "\n")

    if computer == player:
	    print ("tie! no one wins, play again")
    elif player.lower() =="quit":
        exit()
    elif player.lower() == "rock":
        if computer == "paper":
            print("you lose!", computer, "covers", player,"\n")
            player_lives = player_lives - 1
        else:
        	print("you win!", player, "smashes through", computer, "\n")
        	computer_lives = computer_lives - 1
    elif player.lower() == "paper":
        if computer == "scissors":
            print("you lose!", computer, "cuts", player,"\n")
            player_lives = player_lives - 1
        else:
        	print("you win!", player, "coveres", computer, "\n")
        	computer_lives = computer_lives - 1
    elif player.lower() == "scissors":
        if computer == "rock":
            print("you lose!", computer, "smashes", player,"\n")
            player_lives = player_lives - 1
        else:
        	print("you win!", player, "cuts", computer, "\n")
        	computer_lives = computer_lives - 1
        	
    else:
    	print("that's not a valid choice, try again")

    # handle all lives lost for player or AI
    if player_lives is 0:
    	print("Out of lives! You suck at this game. Would you like to play again?\n")
    	choice = input("Y / N")
    	print (choice)

    	if (choice is "N") or (choice is "n"):
    	    print("you choose to quit.")
    	    exit()

    	elif(choice is "Y") or (choice is "y"):
    		#reset the game so that we start all over again
    		player_lives= 5
    		computer_lives= 5
    		player = False
    		computer = choices[randit(0,2)]

    elif computer_lives is 0:
    	print("Computer is out of lives! You rock at this game. Would you like to play again?\n")
    	choice = input("Y / N")
    	print (choice)

    	if (choice is "N") or (choice is "n"):
    	    print("you choose to quit.")
    	    exit()

    	elif(choice is "Y") or (choice is "y"):
    		#reset the game so that we start all over again
    		player_lives= 5
    		computer_lives= 5
    		player = False
    		computer = choices[randit(0,2)]
    else:
        # need to check all of our conditions after checking for a tie
        player = False
        computer = choices[randint(0, 2)]