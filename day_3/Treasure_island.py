
'''
In this script we gonna create a find the treasure game, using if/elif/else statments.
'''




from itertools import count


if __name__ == "__main__":


    while True:

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    

        ''')


        print('Welcom to Treasure Island')
        print ('Your mission is to find the treasure!!!!')
        left_right = input("You're at a cross road, Where do you want to go?  Type 'Left' or 'Right'  ")

        if left_right == 'left':
            print("Good job!")
            wait_swim = input("You came to a lake. theres is an island in the middle of the lake. Type: 'wait' for a boat or 'swim' to swim across  ")
            if wait_swim == 'wait':
                print("Well done, you reached the island ")
                colour = input("There is a house with 3 doors, One red, one yellow and one blue, Which colour dp you choose?  ")
                if colour == 'red':
                    print("Burned by fire")
                    print("Game Over")
                elif colour == 'blue':
                    print("Eaten by beasts")
                    print("Game Over")
                    break
                elif colour == 'yellow':
                    print("Well Done!!!! you reach the Treasure :)")

                else:
                    print("Invalid command")
                    print("Game Over")
                    break
                    
            else:
                print("Attack by shark")
                print("Game Over")
                break

        else:
            print("Fall into a hole :( ")
            print("Game Over")
            continue


