"""
2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The
    function should return the value of x times y. Remember, multiplication can be performed
    as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero
    integers.)
"""

def recursive_multiply(x,y):
    if x == 0:
        return y