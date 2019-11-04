# constants for rows and columns
ROWS = 3
COLUMNS = 4

def main():
    #create a two-dimensional list
    values = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    # fill the list with random numbers
    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(1,100)

    #display the random numbers
    print(values)

#call the main function
main()