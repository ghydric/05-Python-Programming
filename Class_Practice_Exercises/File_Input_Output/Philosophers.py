# This program writes three lines of data to a file

filepath = r"C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\File_Input_Output\philosophers.txt"

def main():
    # Open a file named philosophers.txt
    f = open(filepath, 'w')

    # Write the names of the three philosophers
    f.write('John Locke\n')
    f.write('David Hume\n')
    f.write('Edmund Burke\n')

    # Close the file
    f.close()

# Call the main function
main()