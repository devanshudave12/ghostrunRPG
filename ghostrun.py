attack = ['laser light', 'help of friendly ghost', 'knife', 'metal sword']
# prints the statement
print(f"AVAIALBE options to attack:")
# prints the each element of the list in order from(1to4)
for attacks in range(0, len(attack)):
    print(str(attacks+1)+"."+attack[attacks])

# options given if the player wishes to defend
defend = ['cross sign', 'pray', 'run']

print (f"AVAIALBE OPTIONS TO DEFEND ----MR/MRS GAMER")
for defends in range(0, len(defend)):
    print(str(defends+1)+"."+defend[defends])
