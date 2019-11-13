# Name - Devanshu Dave
# course - Computer Science 30
# period - 4
# Date Created - 06/11/19
# Date last modified - 12-11-19
# Description -  program prints the menu and takes input and loops continuosly

# list for printing locations
locations = ['north', 'south', 'east', 'west']
# list for printing attacks
attacks = ['laser light', 'sword', 'knife']
# list for printing defends options
defends = ['cross sign', 'pray', 'run']


# using the function to define the options variable
def options():
    '''Return a full menu showing options'''
    print(f"GO TO THIS FOLLOWING DIRECTION:")
    for location in locations[:4]:
        print('* ' + location.lower())   # prints the options of location

    print(f"CHOOSE ONE THE ACTION TO ATTACK:")
    for attack in attacks[:3]:
        print('* ' + attack.lower())   # print the options to attack from list

    print(f"CHOOSE ONE OPTION TO DEFEND:")
    for defend in defends[:3]:
        print('* ' + defend.lower())  # prints the defends option from list


# defining the input or action choosen by the gamer
def action_function(action):
    '''return a input choosen by the user'''
    if action in locations:
        print(f"Go! " + action.lower())  # prints input if choosen locations

    elif action in attacks:
        print(f"You have " + action.lower())  # prints input is chooden attack

    elif action in defends:
        print(f"You should be " + action.lower() + "ing")  # defends input

    elif action == "quit":
        quit()      # quit option if want to exit
    else:
        print(f"Invalid!")

print(f"PRESS QUIT IF YOU WANT TO EXIT****")

options()
# while loop for continous game
while True:
    action = input(f"Your choice: ")   # taking input from the user 
    action_function(action.lower())
