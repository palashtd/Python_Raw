# For example, assigning grades (A, B, C) based on marks obtained by a student.
#
# if the percentage is above 90, assign grade A
# if the percentage is above 75, assign grade B
# if the percentage is above 65, assign grade C
# Note: I have used percentage >= to calculate grade.

# Code:
user_mark_percentage = float(input("Enter your mark percentage here: "))

if user_mark_percentage >= 90:
    grade = "A"
elif user_mark_percentage >= 75:
    grade = "B"
elif user_mark_percentage >= 65:
    grade = "C"
elif user_mark_percentage >= 33:
    grade = "D"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")
