"""
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.
"""
# recursive printing function
def print_numbers(n):
    # print n
    print(n)
    # base case 1
    if n == 0:
        return 0
    # base case 2
    elif n == 1:
        return 1
    # recursive case
    else:
        return print_numbers(n-1)

#num = int(input('Enter an integer: '))
#print_numbers(num)

def print_num(n):
    if n > 1:
        print_num(n-1)
    print(n, sep = " ")

print(print_num(4))