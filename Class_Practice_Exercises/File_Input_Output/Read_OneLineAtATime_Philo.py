# This program reads the contents of the philosophers.txt
# file one line at a time
def main():
    # Open a file named philosophers.txt
    f = open(r"C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\File_Input_Output\philosophers.txt", 'r')

    # Read one line at a time
    line1 = f.readline().rstrip('\n')
    line2 = f.readline().rstrip('\n')
    line3 = f.readline().rstrip('\n')

    # Close the file
    f.close()

    # Print the data that was read
    print(line1)
    print(line2)
    print(line3)

# Call the main function
main()