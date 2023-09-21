# Assignment 11: String Manipulation Basics Create a Python program that takes a user's full name as input and prints it in reverse order (last name, first name).
# •	Then, count and display the total number of characters in the full name.
# •	Finally, extract and display the initials of the first and last names.

# Method#1: Using 2wo user inputs
user_first_name = input("Enter your first name here: ").title()
user_last_name = input("Enter your last name here: ").title()
names_list = [user_first_name, user_last_name]
initials = user_first_name[0] + user_last_name[0]
full_name = user_first_name + " " + user_last_name
names_list.reverse()
reverse_name = " ".join(names_list)
total_characters = len(full_name.replace(" ", ""))
print(f"Your full name is: {full_name}\nAssignment's solution: {reverse_name}\nTotal Characters: {total_characters}\nName initials: {initials}")

# Method#2: Using single user input
full_name = input("Enter your full name here: ").title()
names = full_name.split()
reversed_name = " ".join(names[::-1])
total_characters = len(full_name.replace(" ", ""))
initials = names[0][0] + names[-1][0]
print("Reverse name: ", reversed_name)
print("Total characters: ", total_characters)
print("Initionals: ", initials)

# Create by Palash Talukder.