# Problem 4: String Formatting and Validation:
# Design a program that validates email addresses entered by users.
# Prompt the user for an email address and check if it follows the standard email format (e.g., contains "@" and ".").
# Display a message indicating whether the email is valid or not.


user_email = input("Enter your email: ")
char_to_find = "@"
char_to_find2 = "."
if char_to_find in user_email and char_to_find2 in user_email:
    print("It's a valid email address")
else:
    print("It's not a valid email address")
