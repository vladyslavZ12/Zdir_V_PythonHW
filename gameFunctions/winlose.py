from random import randint
#define
def winorlose (status):
    #status will be either won or lost - you're passing this in as an argument
    print("called win or lose")
    print("*********************************")

    print("You", status, "! Would you like to play again")

    choice = input("Y / N")
    print (choice)
    
    if (choice is "N") or (choice is "n"):
        print("you choose to quit.")
        exit()

    elif(choice is "Y") or (choice is "y"):
            #reset the game so that we start all over again
        global player_lives
        global computer_lives
        global player
        global computer
        global choices

        player_lives= 1
        computer_lives= 1
        player = False
        computer = choices[randit(0,2)]