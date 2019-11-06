# Serializing Objects
# Serializing an object is the process of converting the object to a stream of bytes
# that can be saved to a file for later retrieval. In Python, object serialization
# is called pickling.

#output_file = open('mydata.dat', 'wb')
#pickle.dump(object, file)

# this program demonstrates object pickling
import pickle

# main function
def main():
    # controls loop repetition
    again = 'y'

    # open a file for binary writing
    output_file = open(r'C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\Serialization\information.dat', 'wb')
    
    while again.lower() == 'y':

        # get data about a person and save it
        save_data(output_file)

        # does the user want to enter more data?
        again = input('Enter more data? (y/n): ')

    # close the file
    output_file.close()

# the save_data function gets data about a person, stores
# it in a dictionary, and then pickles the dictionary to the
# specified file
def save_data(file):
    # create an empty dictionary
    person = {}

    # get the data for a person and store it in a dictionary
    #person['name'] = input('Name: ')
    #person['age'] = input('Age: ')
    #person['weight'] = float(input('Weight: '))
    
    # another way to do the above
    person.update({'name' : input('Name: '), 'age' : input('Age: '), 'weight' : float(input('Weight: '))})
    
    # pickle the dictionary
    pickle.dump(person, file)

# call the main function
main()