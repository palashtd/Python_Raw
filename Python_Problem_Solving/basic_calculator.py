# Function that can perform basic arithmetic operations (addition, subtraction, multiplication, division).

def calculator():
    total = float(input('Enter your number: '))
    count = 0

    while count < 1:
        operator = input('Enter an operator (+, -, *, /): ')
        user_input1 = float(input('Enter another2 number: '))

        if operator == '+':
            user_total_sym = input('Enter (=) here: ')
            if user_total_sym == '=':
                total += user_input1

        elif operator == '-':
            user_total_sym = input('Enter (=) here: ')
            if user_total_sym == '=':
                total -= user_input1
        elif operator == '*':
            user_total_sym = input('Enter (=) here: ')
            if user_total_sym == '=':
                total *= user_input1
        elif operator == '/':
            if user_input1 == 0:
                print("Error: Division by zero is not allowed.")
                return None
            else:
                user_total_sym = input('Enter (=) here: ')
                if user_total_sym == '=':
                    total /= user_input1
        else:
            print("Invalid operator. Please enter +, -, *, or /.")
            return None

        count += 1

    return total


result = calculator()
print('Result=', result)
