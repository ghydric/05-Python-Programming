"""**Lab 2D: Strings**

**Instructions:**

Write a program that reverses a user inputted string then outputs the new string, in all uppercase letters.

**Bonus:** Add additional functionality, experiment with other string methods.
"""
userString = input("Please type in a string to be reversed and changed to all caps: ")

modifiedString = userString[::-1].upper()

print(modifiedString)