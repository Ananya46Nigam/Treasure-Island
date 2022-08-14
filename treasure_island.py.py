print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island !!")
print("Your mission is to find the treasure.") 
turn=input('You are at a cross road on this abandoned island.Where do you want to go?"left" or "right".').lower()

if turn=="left":
    print("You have come to a lake.")
    swim_or_wait=input("Do you want to \"swim\" or \"wait\" for your boat?").lower()
else:
    print("Too much greed that you didnt wait")
    print("Ooops!You fell in a hole.")
    print("|______GAME OVER______|")
    
if swim_or_wait=="wait":
    print("Well Done !Time for ultimate decision to take.")
    print("You have arrived at a castle unarmed.It has 3 doors.")
    print("Choose the magic door.")
    door=input("Red | Blue | Yellow ?").lower()
else:
    print("Too much greed that you didnt wait")
    print("Ooops!You fell in a hole.")
    print("|______GAME OVER______|")
    
if door=="red":
    print("Ooops!You got burned by fire !!")
    print("|______GAME OVER______|")
elif door=="blue":
    print("Ooops!You got eaten by beasts.")
    print("|______GAME OVER______|")
    
elif door=="yellow":
    print('''
******************************************************************************
                                 _       
                                | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\_\__
 \___\___/|_| |_|\__, |_|  \__,_|\__|_/_/
                  __/ |                  
                 |___/                   

*******************************************************************************

        ''')
    print("|______ YOU FOUND THE TREASURE _____|")
     
else:
    
    print("|______GAME OVER______|")
   
    
    
    




