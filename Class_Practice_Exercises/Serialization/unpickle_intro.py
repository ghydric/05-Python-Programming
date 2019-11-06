# this program demonstrates object unpickling
import pickle

# main function
def main():
    #Indicate the end of the file
    end_of_file = False

    # open a file for binary reading
    input_file = open(r'C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\Serialization\information.dat', 'rb')

    #read to the end of the file
    while not end_of_file:
        try:
            # unpickle/deserialize the next object
            person = pickle.load(input_file)

            # display the object
            display_data(person)

        except EOFError:
            # set the flag to indicate the end
            # of the file has been reached
            end_of_file = True
    
    # close our file
    input_file.close()

# The display_data function displays the person data
# in the dictionary that is passed as an argument
def display_data(person):
    print(f"Name: {person['name']}\nAge: {person['age']}\nWeight: {person['weight']}")

# Call the main function
main()
