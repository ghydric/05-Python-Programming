# This program reads and displays the contents
# of the philosophers.txt file

def main():
    # Open a file named philosophers.txt
    f = open(r"C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\File_Input_Output\philosophers.txt", 'r')

    # Read the file's contents
    f_contents = f.read()

    # Close the file
    f.close()

    # Print the data that was read into memory
    print(f_contents)

# Call the main function
main()