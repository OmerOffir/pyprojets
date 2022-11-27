
'''
The next script mange an auction, the users writes they name and they bids, and the script return who's the winner.

'''

hammer = '''
       ,
      /(  ___________
     |  >:===========`
      )(
'''

auction_data = {}


def new_player(name, bid):
    auction_data[name] = bid

def max_bid():
    max_value = max(auction_data, key=auction_data.get)
    return max_value

if __name__ == "__main__":
    print(hammer)
    print("Welcome to the secret auction program")
    while True:
        name = input("What is your name? ")
        bid = float(input("What is your bis? "))
        new_player(name, bid)
        another_player = input("Are there any other bidders?  Type 'Yes' or 'No  ")
        if another_player == 'No':
            max_bidder_name = max_bid()
            print("The winner is: " + str(max_bidder_name))
            break
        else:
            continue


