"""
1. 
    (Remove text) Write a program that removes all the occurrences of a specified
    string from a text file named pointsOfAuthority.txt. Your program should prompt the user to enter 
    a filename and a string to be removed.

    Points Of Authority - Linkin Park

        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last

        You love the way I look at you
        While taking pleasure in the awful things you put me through
        You take away if I give in
        My life, my pride is broken

        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)

        You love the things I say I'll do
        The way I'll hurt myself again just to get back at you
        You take away when I give in
        My life, my pride is broken

        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)

        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last

        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last

        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)
"""

def main():
    # filepath to use for input and output files
    file_path = r"C:\Users\student\Documents\myGitStuff\Python_Basics_Performance_Assessment\\"
    
    # prompt user for input file
    input_file = input('Please enter a filename: ')

    # create output file name
    output_file = 'removed_text.txt'

    # prompt user for string to be removed from file
    string_to_be_removed = input('Please enter the string to be removed from the file: ')
    
    # Open the input file
    f_in = open((file_path + input_file), 'r')

    # Open the output file
    f_out = open((file_path + output_file), 'w')

    # loop through each line in input file, then replace the string to be removed with nothing
    # and write that line to the output file
    for line in f_in:
        line = line.replace(string_to_be_removed, "")
        f_out.write(line)

    # Close the input file
    f_in.close()

    # Close the output file
    f_out.close()

# Call the main function
main()