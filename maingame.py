# Name - Devanshu Dave
# course - Computer Science 30
# period - 4
# Date Created - 22/11/19
# Date modified - 26/11/19
# Description - the program that works the main game


import characteristics   # import the file  # import the file
import inventory
import map2 # import the file
import time

print("WELCOME TO THE GAME : THE GHOST RUN")
time.sleep(2)
print("HOPE YOU WILL ENJOY THIS GAME")
time.sleep(3)
print("LETS START")
time.sleep(3)
# defines the function for taking input
def get_input_wish(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower()

actions = ["start", "inventory", "characteristics", "quit"]   # list


# implements the input of the user
def action_function(get_action):
    '''input by the user in formatted form'''
    if get_action == "start":
        print("yor are entering the game")
        map2.game1()   # called the function
    elif get_action == "inventory":
        inventory.start_inven()   # called the function
    elif get_action == "characteristics":
        characteristics.get_charac()   # called the function
    elif get_action == "quit":
        print("BYE BYE!")
        quit()   # exit the game if user wishes
    else:
        print("WRONG INPUT!")


# defining the options from the user
def options():
    '''Return a full menu showing options'''
    print(f"Which one would you like to open:")
    for action in actions:
        print('*** ' + action.title())   # prints the options of location


options()
# while true:
while True:
    action_input = get_input_wish("Action: ")
    if action_input:
        action_function(action_input)  # lopped and calling the final one s
