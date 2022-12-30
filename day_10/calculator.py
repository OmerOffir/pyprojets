

calc = '''
 _____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/             JO | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
continue_ans = 'n'
operators_list = ['+', '-', '*', '/', '**']

def calculator(first_num, operator, second_num):
    if operator == '+':
        print(f"{first_num} {operator} {second_num}")
        answer =  first_num + second_num
    elif operator == '-':
        print(f"{first_num} {operator} {second_num}")
        answer =  first_num - second_num
    elif operator == '*':
        print(f"{first_num} {operator} {second_num}")
        answer =  first_num * second_num
    elif operator == '/':
        while second_num == 0:
            print("cant divide by zero")
            second_num = float(input("Please enter new number: "))
        print(f"{first_num} {operator} {second_num}")
        answer = first_num / second_num
    elif operator == '**':
        print(f"{first_num} {operator} {second_num}")
        answer = round(first_num ** second_num, 2)
    else:
        print("Operator is not valid :(")

    return answer

def show_operators():
    for index in operators_list:
        print(index)
    operator = input()
    return operator


        


if __name__ == "__main__":

    print(calc)


    while continue_ans == 'n':
        first_num = float(input("What's the first number?: "))
        print("Choose the wanted operator")
        operator = show_operators()
        second_num = float(input("What's the next number?: "))
        calc_answer = calculator(first_num, operator, second_num )
        print(f'The answer is: {calc_answer}')
        continue_ans = input(f"Type 'y' to contine calculate with {calc_answer}, or type  'n' to start a new calculation: ")

        while continue_ans == 'y':
            first_num = calc_answer
            print("Choose the wanted operator")
            operator = show_operators()
            second_num = float(input("What's the next number?: "))
            calc_answer = calculator(first_num, operator, second_num )
            print(f'The answer is: {calc_answer}')
            continue_ans = input(f"Type 'y' to contine calculate with {calc_answer}, or type  'n' to start a new calculation: ")





