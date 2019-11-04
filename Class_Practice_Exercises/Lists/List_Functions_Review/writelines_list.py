# This program uses the writelines method to save a list of strings to a file

def main():
    # file path for the cities2.txt file
    filepath = ''
    
    # create a list of strings
    cities = ['New York\n', 'Boston\n', 'Atlanta\n', 'Dallas\n']

    # open a file for writing
    outfile = open(filepath, 'w')

    # write the list to the file
    for item in cities:
        outfile.write(item)

    # close the file
    outfile.close()

# call the main function
main()