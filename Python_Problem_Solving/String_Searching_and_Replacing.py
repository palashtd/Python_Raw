# Problem: String Searching and Replacing:
# •	Given a text containing a sample paragraph of text.
# •	Write a Python program that reads this paragraph and searches for a “specific word” and display the number of occurrence of that word.
# •	Replace all occurrences of the word with “replace with” word and display the modified text.

given_paragraph  = "Python is commonly used for developing websites and software, task automation, data analysis,\
 and data visualization. Since it's relatively easy to learn, Python has been adopted by many non-programmers such\
  as accountants and scientists, for a variety of everyday tasks, like organizing finances"
find_words_occurrence = given_paragraph.count("Python")
replace_specific_word = given_paragraph.replace("Python", "PYTHON")
print(f"Number of occurrence(Python) in this paragraph: {find_words_occurrence}\nAfter replace paragraph:\n{replace_specific_word}")