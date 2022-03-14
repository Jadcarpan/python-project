#!/usr/bin/env python
# coding: utf-8
import vlc, time


#Declaration of doors and keys

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}


key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

#Items declaration per room
#Game Room
couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}


#Bedroom 1
queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

light_switch = {
    "name": "light switch",
    "type": "furniture",
}

#Bedroom 2
double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

#living room
dining_table = {
    "name": "dining table",
    "type": "furniture",

}

#declaration of different rooms    
game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

#Declaration of boolean variables for next functions
light_status = False 
dresser_already_checked = 1


all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a], 
    "bedroom 1": [queen_bed, door_a, door_b, door_c, light_switch], 
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, door_c, door_d], 
    "outside": [door_d],
    "door a": [game_room, bedroom_1], 
    "door b": [bedroom_1, bedroom_2], 
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside], 
}


INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


def linebreak():
    
    print("\n\n")

def start_game():
    
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
 
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        duration = 2
        time.sleep(duration)
        player = vlc.MediaPlayer("win.wav")
        player.play()
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'ex\033[4mP\033[0mlore' or '\033[4mE\033[0mxamine'?\n")
        if intended_action.lower() in ("explore","p"):
            explore_room(room)
            play_room(room)
        elif intended_action.lower() in ("examine","e"):
            item = (input("What would you like to examine?\n").strip())
            if (item == "piano"):
                ex_piano(item)
            elif (item == "queen bed"):
                ex_queen_bed(item)
            elif (item == "light switch"):
                light(item)
            elif (item == "double bed"):
                doublebed_check(item)
            elif (item == "dresser"):
                dresser_check(item)
            elif (item == "dining table"):
                food(item)
            elif (item == "cheat"):
                cheat_code(item)
            else: 
                examine_item(item)
        else:
            print("Not sure what you mean. Type 'ex\033[4mP\033[0mlore' or '\033[4mE\033[0mxaminexamine'.")
            play_room(room)
        linebreak()

def cheat_code(cheat):
    player = vlc.MediaPlayer("cheat.wav")
    player.play()
    duration = 1
    time.sleep(duration)
    game_state["keys_collected"].append(key_d)
    play_room(living_room)


def ex_piano(piano):
    global play_room
    global game_state
    print("The piano looks pretty unused due to the amount of dust.")
    decission = input("Do you want to play it? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
    if  decission.lower() in ("no","n"):
        print("You leave the piano alone")
    elif decission.lower() in ("yes","y") and key_a not in game_state["keys_collected"]:
        print("Although you cannot play any instrument, you notice there's something wrong."
                "Stuck under a keyboard key, you find a rusty metal key. ")
        player = vlc.MediaPlayer("piano.wav")
        player.play()
        game_state["keys_collected"].append(key_a)
    elif decission.lower() in ("yes","y") and key_a in game_state["keys_collected"]:
        player = vlc.MediaPlayer("piano.wav")
        player.play()
        print("You have the key already, there's nothing else")
    else:
        print("Not sure what you mean.")
        ex_piano(piano)
    play_room(game_state["current_room"])


def light(light_switch): 
    global play_room
    global game_state
    global light_status
    if light_status == False:
        print("It is rather dark.")
        decission = input("Do you want to switch on the light? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
    else:
        print("It's pretty bright in here.")
        decission = input("Do you want to switch off the light? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
    if  decission.lower() in ("yes","y"):
        player = vlc.MediaPlayer("switch.wav")
        player.play()
        light_status = not light_status
    elif decission.lower() in ("no, n"):
        print("You leave the switch.")
    else:
        print("Not sure what you mean.")
        light(light_switch)
    play_room(game_state["current_room"])
    
#raghav: code edited slightly - Next function makes you search the queen_bed and only lets you find the key if light is switched on and you decide to look under the mattress
    
def ex_queen_bed(queen_bed): #raghav: not sure what should be the arguement of function ex_queen_bed, as in what should come in the brackets ()
    global play_room
    global game_state
    global light_status
    if  light_status == False:
        player = vlc.MediaPlayer("bed.mp3")
        player.play()
        print("there is nothing on the bed")
    else:
        print('''There is light!! You can finally see cleary 
                Choose 1. to check the pillow cover or 
                Choose 2. To check under the mattress, or
                Choose 3. To look under the bed''')
        choice_1 = input()
        if (choice_1 =='2'):
            player = vlc.MediaPlayer("bed.mp3")
            player.play()
            if key_b not in game_state["keys_collected"]:
                print("Congratulations you have found another key")
                game_state["keys_collected"].append(key_b)
            else:
                print("You already have the key, there's nothing else")
        elif (choice_1 == "1" or "3"):
            player = vlc.MediaPlayer("bed.mp3")
            player.play()
            print("there is nothing there")
            ex_queen_bed(queen_bed)
        else:
            print("That's a non-existent choice. We suppose you don't want to check the bed")
            ex_queen_bed(queen_bed)
    play_room(game_state["current_room"])

#ben: bedroom_2 function to check doublebed and get the key of door_C

def doublebed_check(double_bed):
    global play_room
    global game_state
    print('''Another bed, this time with proper illumination.
            Choose 1. to check the pillow cover or 
            Choose 2. To check under the mattress, or 
            Choose 3. To look under the bed''')
    choice_2 = input()
    if (choice_2 =='1'):
        player = vlc.MediaPlayer("bed.mp3")
        player.play()
        if key_c not in game_state["keys_collected"]:
            print("Congratulations you have found another key")
            game_state["keys_collected"].append(key_c)
        else:
            print("You already have the key, there's nothing else")
    elif (choice_2 == "2" or "3"):
        player = vlc.MediaPlayer("bed.mp3")
        player.play()
        print("there is nothing there")
        doublebed_check(double_bed) 
    else:
        print("That's a non-existent choice.")
        doublebed_check(double_bed)        
    play_room(game_state["current_room"])
    

#ben: dresser_check function to find in the dresser the key of door_d

def dresser_check(dresser):
    global dresser_already_checked
    global play_room
    global game_state
    if dresser_already_checked == 2:
        print("There's nothing more to see there")
        play_room(game_state["current_room"])
    print("this dresser look suspicious")
    choice_3 = input("Do you want to open it? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
    while choice_3.lower() not in ("yes","no","y","n"):
        print("Sorry, we couldn't understand your intentions")
        choice_3 = input("Do you want to open it? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
    else:
        if choice_3.lower() in ("yes","y"):
            player = vlc.MediaPlayer("dresser1.wav")
            player.play()
            print("The dresser wont open, but you hear it crack")
            choice_31 = input("Do you want to try again? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
            while choice_31.lower() not in ("yes","no","y","n"):
                print("Sorry, we couldn't understand your intentions")
                choice_31 = input("Do you want to try again? \033[4mY\033[0mes/\033[4mN\033[0mo \n").strip()
            else:
                if choice_31.lower() in ("yes","y"):
                    player = vlc.MediaPlayer("dresser2.wav")
                    player.play()
                    print("You push again, but still stuck")
                    choice_32 = input("Do you want to try again? Kick/Meh \n").strip()
                    while choice_32.lower() not in ("kick","meh"):
                        print("Sorry, we couldn't understand your intentions")
                        choice_32 = input("Do you want to try again? Kick/Meh \n").strip()
                    else:
                        if choice_32.lower() == "kick":
                            player = vlc.MediaPlayer("dresser3.wav")
                            player.play()
                            duration = 3
                            time.sleep(duration)
                            print("You smash the doors of the dresser!")
                            print("...")
                            print("After all this effort, you find the dresser to be completelly empty")
                            print("\nNonetheless, you decide to look under the dresser... and here you are! You find a key!\n")            
                            game_state["keys_collected"].append(key_d)
                            dresser_already_checked = 2
                        elif choice_32.lower() == "meh":
                            print("You made a weird noise that we take as a cowardly way to quit")
                else:
                    print("You leave the dresser")
        else:
            print("You leave the dresser")
    
    play_room(game_state["current_room"])

    
def food(dining_table): 
    global play_room
    global game_state
    print("There are 2 items on the table.\n")
    print("There is a glass of juice and a plate of chicken\n")
    print("Choose 1: To drink juice\n")
    print("Choose 2: To eat chicken\n")
    choice_5 = input()
    while choice_5 not in ("1","2"):
        print("Please enter a valid choice")
        choice_5 = input()
    else: 
        if choice_5 == '1':
            player = vlc.MediaPlayer("drinking.wav")
            player.play()
            duration = 3
            time.sleep(duration)
            print(r"""
                                  88                               88           
                                  88                         ,d    88           
                                  88                         88    88           
                          ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
                         a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
                         8b       88 8PP"       ,adPPPPP88   88    88       88  
                         "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
                          `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88 """)
            print(r"""
                              ██████████████                                                  
                      ████████░░░░░░░░██▒▒██                                                  
                  ▓▓██░░▒▒░░░░░░░░░░░░██▒▒██                                                  
              ████▒▒▒▒░░░░░░░░░░░░░░░░██▒▒██                                                  
            ▓▓▒▒▒▒░░░░░░░░░░░░▓▓▒▒▒▒▒▒██▒▒██                                                  
          ██░░░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
        ██░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
      ██░░░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓██████████████▒▒██                                                  
    ██░░▒▒▓▓▓▓██████████░░            ██▒▒██                                                  
░░██░░▓▓▓▓████                        ██▒▒██                                                  
  ██▒▒████  ▒▒                        ██▒▒██                                                  
░░████                                ██▒▒██                                                  
                                      ██▒▒██                      ██████████████████████      
                                      ██▒▒██                  ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▒▒▒▒▓▓██░░░░██▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▒▒▓▓▒▒██░░░░░░░░██▓▓▓▓▓▓██          
                                      ██▒▒██          ██▓▓▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░██▓▓░░░░▓▓██░░██▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░▓▓▓▓░░░░██▓▓░░██▓▓▓▓██        
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░░░░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░██░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓▓▓██░░██░░██░░██░░████▓▓▓▓▓▓██      
                                      ██▒▒██          ████▓▓▓▓████░░██░░██░░██▓▓▓▓████        
                                      ██▒▒██              ██▓▓▓▓████████████▓▓▓▓██            
                                      ██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒████▓▓▓▓▓▓▓▓▓▓████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓    
                                      ██▒▒██  ██▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██    
                                      ██▒▒██  ██▓▓████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██      
                                      ██▒▒██  ████        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██░░      
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
                                      ██▒▒▒▒██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
                                        ██▒▒██▓▓      ██▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                                        ██▒▒██████    ████▓▓▓▓▓▓▓▓████████▓▓████████▓▓▓▓██████
                                        ░░████████            ██████    ██████                
""")
            print('''YOU HAVE BEEN POISONED... This is the end... Goodbye\n
                              we shall meet soon!!\n\n\n''')
                              
            player = vlc.MediaPlayer("game_over.wav")
            player.play()
            duration = 3
            
            
            game_state = INIT_GAME_STATE.copy()

            start_game()
        elif choice_5 == "2":
            player = vlc.MediaPlayer("eating.wav")
            player.play()
            print("It was good, you wonder who left it there, but now it's time to move") 
    
    play_room(game_state["current_room"])

        
def explore_room(room):
   
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            play_room(current_room)

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter '\033[4mY\033[0mes' or '\033[4mN\033[0mo'\n").strip() == 'yes' or "Y" or "y"):
        player = vlc.MediaPlayer("door.wav")
        player.play()
        play_room(next_room)
    else:
        play_room(current_room)


# In[ ]:


game_state = INIT_GAME_STATE.copy()

start_game()

