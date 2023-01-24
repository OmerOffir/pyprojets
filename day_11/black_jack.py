from random import randrange, sample

balck_jack_photo = '''
                                     _____
        _____                 _____ |6    |
        |2    | _____        |5    || & & |
        |  &  ||3    | _____ | & & || & & | _____
        |     || & & ||4    ||  &  || & & ||7    |
        |  &  ||     || & & || & & ||____9|| & & | _____
        |____Z||  &  ||     ||____S|       |& & &||8    | _____
               |____E|| & & |              | & & ||& & &||9    |
                      |____h|              |____L|| & & ||& & &|
                                                  |& & &||& & &|
                                                  |____8||& & &|

██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔════╝██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║█████╗░░██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══╝░░██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝███████╗╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░╚═╝░░╚═╝                                                      
        
'''
cards = [2,3,4,5,6,7,8,9,10,10,10,10,'ace',
        2,3,4,5,6,7,8,9,10,10,10,10,'ace',
        2,3,4,5,6,7,8,9,10,10,10,10,'ace',
        2,3,4,5,6,7,8,9,10,10,10,10,'ace']

winner = '''
 .----------------.  .----------------.  .-----------------. .-----------------. .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     _____    | || | ____  _____  | || | ____  _____  | || |  _________   | || |  _______     | |
| ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || ||_   \|_   _| | || | |_   ___  |  | || | |_   __ \    | |
| |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || |  |   \ | |   | || |   | |_  \_|  | || |   | |__) |   | |
| |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || |  | |\ \| |   | || |   |  _|  _   | || |   |  __ /    | |
| |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || | _| |_\   |_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || ||_____|\____| | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

'''

loser = '''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   _____      | || |     ____     | || |    _______   | || |  _________   | || |  _______     | |
| |  |_   _|     | || |   .'    `.   | || |   /  ___  |  | || | |_   ___  |  | || | |_   __ \    | |
| |    | |       | || |  /  .--.  \  | || |  |  (__ \_|  | || |   | |_  \_|  | || |   | |__) |   | |
| |    | |   _   | || |  | |    | |  | || |   '.___`-.   | || |   |  _|  _   | || |   |  __ /    | |
| |   _| |__/ |  | || |  \  `--'  /  | || |  |`\____) |  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |  |________|  | || |   `.____.'   | || |  |_______.'  | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''







################################################################################################
def your_cards_split(cards):
    your_cards = list()
    card_one = cards.pop(randrange(len(cards)))
    card_two = cards.pop(randrange(len(cards)))
    your_cards.append(card_one)
    your_cards.append(card_two)
    print('Your cards are: '+str(your_cards))
    return your_cards, cards

def select_house_cards(cards):
    computers_cards = list()
    card_one = cards.pop(randrange(len(cards)))
    card_two = cards.pop(randrange(len(cards)))
    print(f"Computer's first card: {card_one}")
    computers_cards.append(card_one)
    computers_cards.append(card_two)
    return computers_cards, cards


def add_card(cards, your_cards):
    another_card = cards.pop(randrange(len(cards)))
    your_cards.append(another_card)
    print(f"Your cards are: {your_cards} ")
    return cards, your_cards
    

def finish_game_your(your_cards):
    try:
        your_total = sum(your_cards)
        return your_total
    except:
        answer = int(input("Do you want the ace be 10 or 1: "))
        if answer == 1:
            for i, x in enumerate(your_cards):
                if x == 'ace':
                    your_cards[i] = 1
            total_sum = sum(your_cards)
            return total_sum
        else:
            for i, x in enumerate(your_cards):
                if x == 'ace':
                    your_cards[i] = 10
            total_sum = sum(your_cards)
            return total_sum
        

                
def finish_game_compuer(computers_cards):
    try:
        computers_cards = sum(computers_cards)
        return computers_cards
    except:
        for i, x in enumerate(computers_cards):
            if x == 'ace':
                computers_cards[i] = 1
        total_sum_1 = sum(computers_cards)
        for i, x in enumerate(computers_cards):
            if x == 'ace':
                computers_cards[i] = 10
        total_sum_2 = sum(computers_cards)
        
        if total_sum_1 > total_sum_2  and total_sum_1 <= 21:
            return total_sum_1
        elif total_sum_2 > total_sum_1 and total_sum_2 <= 21:
            return total_sum_2



def end_game(your_cards, computers_cards):
    your_sum = finish_game_your(your_cards)
    compuyer_sum = finish_game_compuer(computers_cards)

    if your_sum > compuyer_sum  and your_sum <= 21:
        print(f"Compuer's cards are: {computers_cards}")
        print(winner)
    else:
        print(f"Compuer's cards are: {computers_cards}")
        print(loser)




if __name__ == "__main__":
    print (balck_jack_photo)
    game_answer = input('Do you want ot play game og Blackjak? Type "y" or "n": ')
    if game_answer == 'y':
        print("let's go!")
        your_cards, new_cards = your_cards_split(cards)
        computers_cards, new_cards = select_house_cards(new_cards)
        answer = input("Type 'y' to get another card, type 'n to pass: '")
        while answer == 'y':
            new_cards, your_cards = add_card(new_cards, your_cards)
            answer = input("Type 'y' to get another card, type 'n to pass: '")
        else:
            end_game(your_cards, computers_cards)
    else:
        exit()

