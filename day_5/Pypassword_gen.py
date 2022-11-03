

'''
 This script will generate our new password

'''
import random
import string

def pass_gen(num_of_lerrers, num_of_symbols, number_of_num ):
    
    letters = ''.join((random.choice(string.ascii_lowercase) for i in range(num_of_lerrers)))
    digits = ''.join((random.choice(string.digits) for i in range(number_of_num)))
    symbols = ''.join((random.choice(string.punctuation) for i in range(num_of_symbols)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits + symbols)
    random.shuffle(sample_list)
    # convert list to string
    final_password = ''.join(sample_list)
    return final_password
    

if __name__ == "__main__":
    

    print("Welcome to the password generator! :)")

    num_of_lerrers = int(input("How many letters would you like in your password? "))
    num_of_symbols = int(input("How many symbols would you like? "))
    number_of_num = int(input("How many numbers would you like? "))

    pass_word = pass_gen(num_of_lerrers, num_of_symbols, number_of_num )

    print(f"Your password is: {pass_word}")


