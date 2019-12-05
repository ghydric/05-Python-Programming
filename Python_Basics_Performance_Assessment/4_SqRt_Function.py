"""
4. 
    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned. 

        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721
"""
# import needed math library for square root
import math

# print column headers
print('Number    Square Root')

# loop through each number from 0 to 20, display the number padded 3
# next to its square root padded 12 and limited to 4 decimal places
for i in range(0,21):
    print(f"{i:3}    {math.sqrt(i):12.04f}")
