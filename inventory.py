# Name - Devanshu Dave
# course - Computer Science 30
# period - 4
# Date Created - 22/10/19
# Description - this code prints the inventory which you have to attack/defend

print("              INVENTORY       ")

# making nested dictionary
attack = {
    'laserlight': {
       'HP': '18',
       'damage': '91',
       'location': 'bed room',
       'Description': 'makes more damage to the ghost',
        },

    'knife': {
     'HP': '11',
     'damage': '67',
     'location': 'kitchen area',
     'Description': 'makes temporary damage to the ghost',
        },

    'sword': {
     'HP': '18',
     'damage': '89',
     'location': 'rest room',
     'Description': 'makes the ghost loose easily',
        },

   }
# describing each values  from the dictionary with the help of loops
for attacking, attack_info in attack.items():
    print(f"\nattacking: {attacking}")
    damage = f"{attack_info['damage']}"
    HP = f"{attack_info['HP']}"
    location = attack_info['location']
    Description = attack_info['Description']

# prints each values of the dictionary
    print(f"\tdamage: {damage.title()}")
    print(f"\tHP: {HP.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tdescription: {Description.title()}")

# making nested dictionary
defence = {
    'cross sign': {
       'HP': '18',
       'damage': '+2',
       'location': 'main door',
       'Description': 'makes temporary defence from the ghost',
        },

    'run': {
     'HP': '-11',
     'damage': '0',
     'location': 'main door',
     'Description': 'save temporary from the ghost but still have to attack',
        },

    }
# describing the values of the dictionary
for defend, defence_info in defence.items():
    print(f"\ndefend: {defend}")
    damage = f"{defence_info['damage']}"
    HP = f"{defence_info['HP']}"
    location = defence_info['location']
    Description = defence_info['Description']

#  printing each values of the dictonary after describing
    print(f"\tdamage: {damage.title()}")
    print(f"\tHP: {HP.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tdescription: {Description.title()}")

print('----------------------------------------------------------------------')
