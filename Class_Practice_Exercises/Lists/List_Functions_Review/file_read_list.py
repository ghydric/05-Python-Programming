# This program uses the readlines method to read a file's contents into a list

def main():
    # file path for the cities2.txt file
    filepath = ''
    
    # create a list of strings
    cities = ['New York\n', 'Boston\n', 'Atlanta\n', 'Dallas\n']

    # open a file for writing
    infile = open(filepath, 'r')

    # read the contents of the file into a list
    cities_read_in = infile.readlines()

    # close the file
    infile.close()

    # strip the \n from each element
    index = 0
    while index < len(cities_read_in):
        cities_read_in[index] = cities_read_in[index].rstrip('\n')
        index++
        
# call the main function
main()