
'''
This script calculat the price each person needs to pay 
after a visit to restorant

'''

def tip_calc(bill_price, percent):
    tip = bill_price * (percent/100)
    print(f"{percent}% of {bill_price} $ is: {tip}")
    return tip

def calculation(tip, bill_price, num_of_people ):

    total_tip = tip_calc(bill_price, tip)
    total_price = bill_price + total_tip
    each_person = total_price / num_of_people
    each_person = round(each_person, 2)
    return each_person


if __name__ == "__main__":

    print("Welcome to the tip calculator")
    total_price = float(input ("What was the total bill ? $"))
    num_of_people = int(input ("How many people to split the bill ?"))
    tip = int(input ("What percentage tip would you like to give? 10, 12 or 15?"))
    # Now we call the function for calc the bill
    person_price = calculation(tip, total_price, num_of_people )
    print(f"Each person should pay: {person_price} $")


