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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
decesion_a = input('Youre at a cross roads. Where do you want to go? Type "left" or "right" ')
decesion1 = decesion_a.lower()
if decesion1 == "left":
  decesion_b = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
  decesion2 = decesion_b.lower()
  if decesion2 == "wait":
    decesion_c = input("You arrive at the island. There is a house with 3 doors. One red, one yellow and one blue. Which color do you chose? ")
    decesion3 = decesion_c.lower()
    if decesion3 == "yellow":
        print("You open the door and a cuddly dog is awaiting with a golden magical key. What do you do? Take the key or cuddle the dog?")
    elif decesion3 == "red":
        print("Unfortunetly the room behind the red door is full of flames and you are burnt to a crisp, or maybe you are so chill that you put out the flames with your chillness, but I don't know if you're chill like that so TBD on that one... GAME OVER")
    elif decesion3 == "blue":
        print("Unfortunetly the room behind the blue door is full of knomes and they force you to join the professional knome wresling league. After months of blood sweat and tears you are finally crowned the WORLD CHAMPION of PROFESSIONAL KNOME WRESTLING, so who's the real winner here.... GAME OVER")
      
    else:
      print("Dude seriously I said there were only three doors, why didn't you pick one? GAME OVER")
      
  else:
    print("Unfortunetly you are attacked by the wild Lockness Monster and don't make it to the island, but you do get your picture taken for the news so I guess that's something!... GAME OVER")
    
else:
  print("Unfortunetly you wander aimlessly until nightfall and realize you're wasting your time so you catch an uber home... GAME OVER")

