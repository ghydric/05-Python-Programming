"""
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
"""
### initialize variables
# dictionary holding all the alphabet letters and their corresponding codes as values
enc_dic = {
    'a' : '9',
    'A' : '8',
    'b' : '7',
    'B' : '6',
    'c' : '5',
    'C' : '4',
    'd' : '3',
    'D' : '2',
    'e' : '1',
    'E' : '0',
    'f' : '`',
    'F' : '~',
    'g' : '!',
    'G' : '@',
    'h' : '#',
    'H' : '$',
    'i' : '%',
    'I' : '^',
    'j' : '&',
    'J' : '*',
    'k' : '(',
    'K' : ')',
    'l' : '-',
    'L' : '_',
    'm' : '+',
    'M' : '=',
    'n' : '[',
    'N' : '{',
    'o' : ']',
    'O' : '}',
    'p' : '\',
    'P' : '|',
    'q' : ';',
    'Q' : ':',
    'r' : '<',
    'R' : '>',
    's' : 'q',
    'S' : 'w',
    't' : 'e',
    'T' : 'r',
    'u' : 't',
    'U' : 'y',
    'v' : 'u',
    'V' : 'i',
    'w' : 'o',
    'W' : 'p',
    'x' : 'a',
    'X' : 's',
    'y' : 'd',
    'Y' : 'f',
    'z' : 'g',
    'Z' : 'h'
}
# filepath for input file
input_file = 'C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\Dictionaries_Sets\decoded_text.txt'
# filepath for output file
output_file = 'C:\Users\student\Documents\myGitStuff\05-Python-Programming\Class_Practice_Exercises\Dictionaries_Sets\encoded_text.txt'

