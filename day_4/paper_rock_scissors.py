
'''
 This project program "Rock, paper scissors" game, uses the "random" library 
'''

import random 

def radom_fun():
    number = random.randint(0,2)
    return number

def winner(choose, computer_choose):

    if choose == 0 and computer_choose == 2:
        print("You are the Winner!!! ๐ ")
        return True
    elif choose == 1 and computer_choose == 0:
        print("You are the Winner!!! ๐ ")
        return True
    elif choose == 2 and computer_choose == 1:
        print("You are the Winner!!! ๐ ")
        return True
    elif choose == computer_choose:
        print("It's a tie ๐ต")
        return False
    else:
        print("You loss try again ๐๐ฅ")
        return False


if __name__ == "__main__":

    while True:

        rock_paper_scissors_list = ["๐","๐งพ", "โ๏ธ" ]

        print("Welcome to Rock , Paper Scissors game !!!! ๐ฎ ")
        choose =int(input("What do you choose?  Type 0 for Rock ๐ , 1 for Paper ๐งพ  or 2 for Scissors  โ๏ธ  "))

        print(f"You have chosen : {rock_paper_scissors_list[choose]}")

        computer_choose = radom_fun()

        print(f"The compuer choose is {rock_paper_scissors_list[computer_choose]}")

        answer = winner(choose, computer_choose )

        if answer:
            break
        else:
            continue


    

