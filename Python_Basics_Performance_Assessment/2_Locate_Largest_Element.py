"""
2.
    (Locate the largest element) Write the following function that returns the location
    of the largest element in a two-dimensional list:
    
    def locateLargest(a):
        The return value is a one-dimensional list that contains two elements. These
        two elements indicate the row and column indexes of the largest element in the
        two-dimensional list. Write a test program that prompts the user to enter a 
        two-dimensional list and displays the location of the largest element in the list. 
    
    Here is a sample run(You don't have to mimic this, this is just a guide):

        Enter the number of rows in the list: 3
        Enter a row: 23.5  35  2    10
        Enter a row: 4.5   3   45   3.5
        Enter a row: 35    44  5.5  11.6
        The location of the largest element is at (1,2)
"""
# function that locates the largest value's index in a 2 dimensional list and returns the index
def locateLargest(a):
    """
    # initialize max value
    max = 0
    # initialize max_index
    max_index = (0,0)
    # initialize row and column
    row = 0
    col = 0
    # loop through row
    for r in a:
        # loop through col
        for c in a:
            # if c is greater than max value, make max the value of c
            if c > max:
                max = c
                # set max_index to current row and col
                max_index = (row, col)
            # add 1 to col
            col = col + 1
        # reset col to 0
        col = 0
        # add 1 to row
        row = row + 1
    # return the max index
    return max_index
"""
    index = a.index(max(a))
    return index
def main():
    # get user input for number of rows and columns
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # create the two dimensional array
    arr = [[int(input('Enter a number: ')) for i in range(cols)] for j in range(rows)]
    # for testing, show the 2 dimensional array
    for row in arr:
        print(row)
    # get the largest index
    ind = locateLargest(arr)
    # print out the largest index
    print(ind)
main()