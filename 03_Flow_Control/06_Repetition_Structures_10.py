"""
10. Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #
"""
rows = 6
cols = 7
i = 0 # row iterator

space = " "

# start looping through rows
while i < rows:
    print("#",end="") # each line begins with #
    
    # begin looping through columns
    for t in range(cols):
        if t == i: # if column matches row
            print(f"{space*i}#",end="") # print number of spaces that equal what row number
    i += 1 # increase row
    print() # go to next row
