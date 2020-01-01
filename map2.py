import random     # import random function
dirs = (0, 0, 0, 0)   # value default set


class rooms:
    def __init__(self, inventory, allarea):
        self.inventory = inventory
        self.all_area = allarea

    def Enternce_way(self):
        # print("ssfasfsa")
        print(self.all_area[0].get("msg"))
        # all_area[0].update(msg='You exited from the House')
        msg = 'You exited from the House'
        return msg

    def Livingroom(self):
        # defined the livingroom and priinting it
        print(self.all_area[1].get("msg"))
        #  printing the message
        msg = 'You are back in to the Living room!! Nothing found !'
        return msg

    def Garrage(self):
        print("You Entered the Garden")
        print(self.all_area[2].get("msg"))
        # all_area[2].update(msg='You are back in Garrage!! Nothing found !  ')
        msg = 'You are back in Garrage!! Nothing found !  '
        # all_area[2].update(inv='')
        return msg

    def Boss(self):
        winlose = ['win', 'lose']   # fight with random picker
        print("Be Ready for the fight!! Yor are in front of boss")
        while True:
            fig = input("Press F to fight or Press any key to Exit")
            if fig == 'f' or fig == 'F':
                result = random.choice(winlose)   # randomly picks won or lost
                print("You  " + result)    # prints the result
                break
            else:
                map(inventory)
                print("You are at Main Door")
                break

        # printing the message we the gamer goes again in the room
        msg = 'You are back in Hall!! Nothing found !  '
        return msg

    def Garden(self):
        # print("You Entered the Garden")
        print(self.all_area[4].get("msg"))
        msg = 'You are back in Garden!! Nothing found !  '
        # all_area[4].update(inv='gotit')
        return msg

    def map(self):

        try:
            north = rooms[currentRoom]['north']
        except:
            north = ""
        try:
            south = rooms[currentRoom]['south']
        except:
            south = ""
        try:
            east = rooms[currentRoom]['east']
        except:
            east = ""
        try:
            west = rooms[currentRoom]['west']
        except:
            west = ""

#  map code
        n = "LivingRoom(N)"     # making map
        s = "Garden(S)"        # giving south direction
        vert_line = "|"      # draws the vertical line of the map
        hzt_line = "-- Boss(W) -- Main Door(M) -- Garrage(E) --"  # hztline
        print(north.center(30))
        print("")
        print(vert_line.center(30))
        print(n.center(30))
        print(vert_line.center(30))
        print(west + hzt_line.center(30 - len(west) * 2) + east)
        print(vert_line.center(30))
        print(s.center(30))
        print(vert_line.center(30))
        print("")
        print(south.center(30))
        print("Inventory items " + str(self.inventory))
        print("")


# defining the game
def game1():
    all_area = [
               {'name': 'Enternce_way', 'direction': dirs,
                'msg': 'You are in the enterance room', 'inv': ''},
               {'name': 'Livingroom', 'direction': dirs,
                'msg': 'You are in Living room! ! You have found Sword',
                'inv': 'Sword'},
               {'name': 'Garrage', 'direction': dirs,
                'msg': 'You are in the Garrage , You have found Armour!!',
                'inv': 'Armour'},
               {'name': 'Boss', 'direction': dirs,
                'msg': 'You entered in Boss Room', 'inv': ''},
               {'name': 'Garden', 'direction': dirs,
                'msg': 'You are in the Garden You have found Key!!',
                'inv': 'Key'}
              ]        # dictonary FOR THE GAME
    inventory = []        # will come in side this lisr inventory
    room = rooms(inventory, all_area)
    stuck = True
    room.map()    # room .map is called
    print("You are in Entrance Room")
    last_location = 'B'
    dir_list = ['N', 'S', 'W', 'E', 's', 'w', 'e', 'n']
    inv_list = ['Sword', 'Armour', 'Key']   # list of inventory

#  CODE TO TELL PYTHON IF THIS IS INPUT THEN  FOLLOW THIS AND IF NOT THEN THIS
    while True:
        choice = input("Select direction N E W S OR Q to Quit the Game")
        if not (choice == 'Q' or choice == 'q'):
            if choice in dir_list:
                if (choice == 'N' or choice == 'n'):
                    if last_location == 'B':
                        abc = room.Livingroom()
                        all_area[1].update(msg=abc)
                        last_location = 'N'
                    else:
                        print("Not allowed! only way to enterance E")
                    while True:
                        choice = input("Press M to move back to Main door  ")
                        if choice == 'M' or choice == 'm':
                            last_location = 'B'
                        if all_area[1].get("inv") not in inventory:
                            inventory.append(all_area[1].get("inv"))
                            # all_area[1].update(inv='')
                            room.map()   # called the function
                            print("You are at Main Door")
                        break
                elif choice == 'S' or choice == 's':
                    if last_location == 'B':
                        abc = room.Garden()  # called the function
                        all_area[4].update(msg=abc)
                        last_location = 'S'
                    else:
                        print("Not allowed! only way to enterance E")
                    while True:
                        choice = input("Press M to move back to Main door  ")
                        if choice == 'M' or choice == 'm':
                            last_location = 'B'
                        if all_area[4].get("inv") not in inventory:
                            inventory.append(all_area[4].get("inv"))
                            room.map()    # called for map
                            print("You are at Main Door")
                        break

                elif choice == 'E' or choice == 'e':
                    if last_location == 'B':
                        room.Garrage()
                        last_location = 'E'
                    else:
                        print("Not allowed! only way to enterance E")
                    while True:
                        choice = input("Press M to move back to Main door  ")
                        if choice == 'M' or choice == 'm':
                            last_location = 'B'
                            if all_area[2].get("inv") not in inventory:
                                inventory.append(all_area[2].get("inv"))
                            room.map()   # called the function
                            print("You are at Main Door")
                            break
                else:
                    choice == 'W' or choice == 'w'
                    if not inv_list[0] in inventory:
                        print("You Cannot Enter to this Room!! \
                        You have to find [Sword] to fight with Boss")
                        continue
                    elif not inv_list[1] in inventory:
                        print("You Cannot Enter to this Room!! \
                        You have to find [Armour] for protection")
                        continue
                    elif not inv_list[2] in inventory:
                        print("You Cannot Enter to this Room!!\
                        You have to find [Key] to enter the room")
                        continue
                    else:
                        room.Boss()   # called the function
                        cice = input("Press P to Play again")
                        if (cice == 'P' or cice == 'p'):
                            all_area = [{'name': 'Enterway', 'direction': dirs,
                                         'msg': 'You are in enterance room',
                                         'inv': ''},
                                        {'name': 'Living', 'direction': dirs,
                                         'msg': 'You are in Living room! ,\
                                          You have found Sword',
                                         'inv': 'Sword'},
                                        {'name': 'Garrage', 'direction': dirs,
                                         'msg': 'You are in the Garrage , \
                                          You have found Armour!!',
                                         'inv': 'Armour'},
                                        {'name': 'Boss', 'direction': dirs,
                                         'msg': 'You entered GHOST Room',
                                         'inv': ''},
                                        {'name': 'Garden', 'direction': dirs,
                                         'msg': 'You are in the Garden You \
                                          found Key!!',
                                         'inv': 'Key'}
                                        ]
                            inventory = []
                            room = rooms(inventory, all_area)
                            stuck = True   # set as stuck is equal to true
                            room.map()   # called the function
                            print("You are in Entrance Room")
                            last_location = 'B'
                            dir_list = ['N', 'S', 'W', 'E', 's', 'w', 'e', 'n']
                            inv_list = ['Sword', 'Armour', 'Key']
                            continue
                        else:
                            break

            else:
                room.map(inventory)    # called for inventory
                print("Select the value from N E W S OR Q to Quit the Game")
                print()
                continue
        else:
            print("Good Bye.. Have a Nice day ")   # goodbye message
            break
# game1()
