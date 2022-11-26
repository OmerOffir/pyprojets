
'''
The script is calculator, the computer asks from the user to set a number, then an operator and then anther number,the script
prints the result.

use:
fumctions
operators: *, /, +, -, **

'''
num1 = float(input('Please enter a number: '))
operator = input('Please enter an operator: ')
num2= float(input('Please enter another number: '))

def function(num1, operator, num2):
    
    if (operator == '+'):
        Total = round(num1 + num2, 2)
        
    elif (operator == '-' ):
        Total = round(num1 - num2, 2)
        
    elif (operator == '*'):
        Total = round(num1 * num2, 2)
        
    elif (operator == '/'):
        while num2 == 0:
            print('cant divide by zero')
            num2 = float(input('please enter another number: '))

        Total = round(num1 / num2, 2) 

    elif (operator == '**'):
         Total = round(num1 ** num2, 2)
         
    else:
        Total = ('operator is not valid')
       
    return Total

result = function(num1, operator, num2)
print(f"= {result} " )
