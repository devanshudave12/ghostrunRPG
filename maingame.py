# import sys
# from tabulate import tabulate
# import characteristics
import map
# import inventory
# import continuousgameplay




def get_input_wish(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower() 
# def play():
#     '''Return a menu in formated form''''
action = ["map","inventory","characteristics","quit"]

def options():
    '''Return a full menu showing options'''
    print(f"Which one would you like to open:")
    for actions in action[:4]:
        print('*** ' + actions.title())   # prints the options of location

options()
# while true:
action_input = get_input_wish("Action: ")

def  action_function():
    '''input by the user in formatted form'''
    if action_input == "map":
        startgame()

# def get_input_wish(message):
#     """Get user input and convert the string to lowercase"""
#     action_input = input(message)
#     return action_input.lower()
#
# def choose_map():
#     '''returns the printed map for the player'''
#



# choice = input("action:  ")
