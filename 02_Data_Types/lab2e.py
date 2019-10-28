"""## Lab 2E: Count Words

**Instructions:**

Write a program that takes a string as user input then counts the number of words in that sentence.

**Bonus:** Add additional functionality, experiment with other string methods.

ex: Output number of characters, number of uppercase letters, etc...
"""
userInput = input("Please enter a string: ")
words = len(userInput.split(" "))
letters = userInput
uppercase = 0
lowercase = 0
for i in letters:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    else:
        continue
statement = "There are {} words, {} letters, {} uppercase letters, and {} lowercase letters."
print(statement.format(words, len(letters), uppercase, lowercase))



