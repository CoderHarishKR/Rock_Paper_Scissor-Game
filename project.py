# This Python code is a  


import random # random module imported for number generation

user_win = 0 # Two variable are declared for storing the points 
pc_win = 0

option = ["rock", "paper", "scissor"] # A list that consist of options for the game. option[0]=rock, option[1]=paper, option[2]=scissor.

while True: # A while loop without condition.
    user_input = input("Rock, Paper, Scissor or Q for Quit: ").lower() # User input for the game.

    if user_input =='q': # Check whether the user input is for quitting the game.
        print("\nYou Quit")
        break

    if user_input not in option: # Check whether the user enter an invalid choice.
        print("\nInvalid Option")
        continue

    random_number = random.randint(0,2) # A random number generated between 0 and 2 including both numbers.
    pc_selection = option[random_number] # A random number is generated and the options in list are accessed using that number by considering it as index.
    print("\nPC Selected: ",pc_selection) # The option is displayed to user.

    #Checking the user input and pc selection using if loop and user point is incremented accordingly.

    if user_input == "rock" and pc_selection =="scissor": 
        print("You Won..!!!")
        user_win +=1
    
    elif user_input == "paper" and pc_selection =="rock":
        print("You Won..!!!")
        user_win +=1
    
    elif user_input == "scissor" and pc_selection =="paper":
        print("You Won..!!!")
        user_win +=1

    else:
        print("You Lost")
        print("I Win..!!!")
        pc_win +=1 # The pc point is incremented when the above conditions become false.

print("Your Point:",user_win) # The points are displayed to user.
print("My Point:",pc_win)

print("GoodBye")
              
    
