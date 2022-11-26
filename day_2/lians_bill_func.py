price = float(input(' Please enter the price of the bill '))
people = int(input(' Please enter the number of people who are eating '))
Tip = float(input(' Please enter how much tip do you have to leave in percent '))

def function(price, people, Tip):
    Total_price = (price * Tip/100 + price )/ people
    return Total_price


    
Total_price = function(price, people, Tip) 
Total_price = round(Total_price, 2)
print(f' each person neads to pay: {round(Total_price, 2)} $ ')