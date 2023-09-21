# Problem 1: Handling Division by Zero
# Guidelines:
# •	Write a Python program that takes two numbers as input from the user.
# •	Use a try-except block to handle the division operation.
# •	If the user tries to divide by zero, catch the exception and print an error message.
# Only Python Raw Code. Use the below code on your code editor.

try:
    while True:
        try:
            user_num1 = float(input("Enter your number here: "))
            user_num2 = float(input("Enter your number here: "))
            result = user_num1 / user_num2
            print(result)
            if result:
                break
            else:
                continue
        except ZeroDivisionError:
            print("Division by zero not allowed")
except ValueError:
    print('Please enter correct value')

# Create by Palash Talukder.
