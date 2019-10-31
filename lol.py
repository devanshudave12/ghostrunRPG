locations = ['north','south','east','west']

attacks = ['laser light','sword','knife',]

defends = ['cross sign','pray','run']

print("GO TO THIS FOLLOWING DIRECTION:")
for location in locations[:4]:
    print('* ' + location.title())

print("CHOOSE ONE THE ACTION TO ATTACK:")
for attack in attacks[:3]:
    print('* ' + attack.title())

print("CHOOSE ONE OPTION TO DEFEND:")
for defend in defends[:3]:
    print('* ' + defend.title())

action = input("your choice: ")

if action in locations:
    print("go! " + action.title())

elif action in attacks:
    print("you have " + action.title())

elif action in defends:
    print("you should" + action.title())

else:

    print("Invalid!")
