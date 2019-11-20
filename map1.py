

location_map  = { 'Bed room' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'sword'
                },

            'Kitchen' : {
                  'north' : 'Bed room',
                  'east'  : 'Living Room',
                  'item'  : 'knife'
                },
            'Rest Room' : {
                  'west'  : 'Bed room',
                  'south' : 'Living Room',
                  'east'  : 'Main door',
                  'item'  : 'laserlight'
                },
            'Living Room' : {
                  'north' : ' Rest Room',
                  'west'  : 'Kitchen',
                  'item'  : 'ghost'
                },
            'Main door' : {
                  'west'  : 'Dining Room'
            }
        }

room = {"Living Room": "Main ghost area",
          "kitchen": "main weapons area",
          "bed room": "mainly ghost found",
          "Rest area": "can have a rest"
          }

def list_making(dictonary,list):
    """Create a list from elements of a dictionary"""
    for x in dictionary:
        list.append(x)

def
