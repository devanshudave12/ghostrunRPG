# Name - Devanshu Dave
# course - Computer Science 30
# period - 4
# Date Created - 24/10/19
# Description - this code prints the locations of the gamer using loops


# simple dictonary
location_game = {
     'kitchen': 'centre of the house',
     'bed room': 'main centre of the ghost',
     'rest room': 'main place for the gamer',
     'main door': 'main entrance to defeat the ghost'
     }

# printing each values from the dictonary with the help of the loops
for name, location in location_game.items():
    print(f"you are in {name.title()} which is the {location.title()}.")
