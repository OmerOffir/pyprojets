

'''
 This script will create the "FizzBuzz" game.

Rules:
Players generally sit in a circle. The player designated to go first says the number "1", 
and the players then count upwards in turn.
However, any number divisible by three is replaced by the word "fizz" and any number divisible by five by the word "buzz".
Numbers divisible by both three and five (i.e. divisible by 15) become "fizzbuzz". 
A player who hesitates or makes a mistake is eliminated.

For example, a typical round of fizz buzz would start as follows:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz ....
'''




if __name__ == "__main__":

    print ("Start the FizzBuss game...")

    for number in range(1,101):
        if number % 3 == 0 :
            if number % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif number % 5 == 0 :
            if number  % 3 == 0:
                print("FizzBuzz")
            else:
                print ('Buzz')
        else:
            print(number)
        


        