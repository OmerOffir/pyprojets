
'''
 This project program "Rock, paper scissors" game, uses the "random" library 
'''

import random 

def radom_fun():
    number = random.randint(0,2)
    return number

def winner(choose, computer_choose):

    if choose == 0 and computer_choose == 2:
        print("You are the Winner!!! 🏆 ")
        return True
    elif choose == 1 and computer_choose == 0:
        print("You are the Winner!!! 🏆 ")
        return True
    elif choose == 2 and computer_choose == 1:
        print("You are the Winner!!! 🏆 ")
        return True
    elif choose == computer_choose:
        print("It's a tie 😵")
        return False
    else:
        print("You loss try again 😟🥈")
        return False


if __name__ == "__main__":

    while True:

        rock_paper_scissors_list = ["🌑","🧾", "✂️" ]

        print("Welcome to Rock , Paper Scissors game !!!! 🎮 ")
        choose =int(input("What do you choose?  Type 0 for Rock 🌑 , 1 for Paper 🧾  or 2 for Scissors  ✂️  "))

        print(f"You have chosen : {rock_paper_scissors_list[choose]}")

        computer_choose = radom_fun()

        print(f"The compuer choose is {rock_paper_scissors_list[computer_choose]}")

        answer = winner(choose, computer_choose )

        if answer:
            break
        else:
            continue


    

