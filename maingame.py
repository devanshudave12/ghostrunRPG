locations = ['*north','*south','*east','*west']

attacks = ['*laser light','*sword','*knife',]

defends = ['*cross sign','*pray','*run']

print("GO TO THIS FOLLOWING DIRECTION:")
for location in locations[:4]:
    print(location.title())

print("CHOOSE ONE THE ACTION TO ATTACK:")
for attack in attacks[:3]:
    print(attack.title())

print("CHOOSE ONE OPTION TO DEFEND:")
for defend in defends[:3]:
    print(defend.title())

action = input("your choice:")

if action == locations:
    print(f"go! + {locations.title()}")

if action == attacks:
    print(f"you have + {attacks.title()}")

if action == defends:
    print(f"you used + {defend.tittle()}")

else:
    print("Invalid!")
