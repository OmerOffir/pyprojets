'''
 In this script we program  the hungman gameS

'''

from multiprocessing.managers import ListProxy
from re import L
from hungman_worlds import words
import random



stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===============
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===============
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===============
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
===============
''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
===============
''', '''

    +---+
    |   |
    O   |
        |
        |
        |
===============
''', '''

    +---+
    |   |
        |
        |
        |
        |
===============
''']




def compuer_choice():

    word = random.choice(words.list)
    return word

def num_of_letters(word):

    list_of_ = []
    num = len(word)
    for i in range(num):
        list_of_.append(' _ ')
    print(f"Your word has {num} letters")
    number_of_letters = ''.join(list_of_)
    print(number_of_letters)

    return list_of_
    

def letter_in_word(letter, word):

    list_1 = []

    if letter in word:
        for i, ltr in enumerate(word):
            if ltr == letter:
                list_1.append(i)
        # print(list_1)
        return list_1
    else:
        print (f"You guessed {letter}, that's not in the word. you lose a life")        
        return False

def replace_fun(letter_index, blank_list, letter ):
    
    for index in letter_index:
        blank_list[index] = letter
    blank_list = ''.join(blank_list)
    print(blank_list)
    if ' _ ' in blank_list:
        return blank_list
    else:
        return True

    
def wrong_answer(stage, list_2, word):
    stage -= 1
    if stage >= 0 :
        print(stages[stage])
        print(list_2)
        print(" ")
        return stage
        
    else:
        print("You lost- GmaeOver")
        print(f"The word was: {word}")
        return stage



    
    


if __name__ == "__main__":


    print ("Welcom to Hungman game")
    print(stages[0])
    stage = 7

    word = compuer_choice()
    blank_list = num_of_letters(word)

    while stage >= 0:

        letter = input("Please select a letter ")

        letter_index = letter_in_word(letter, word)

        if letter_index != False:
            answer = replace_fun(letter_index, blank_list, letter)
            if answer == True:
                print("You won!")
                break
                
        else:
            try:
                stage = wrong_answer(stage, answer, word)
            except:
                blank = ''.join(blank_list)
                stage = wrong_answer(stage, blank, word)



            
           



