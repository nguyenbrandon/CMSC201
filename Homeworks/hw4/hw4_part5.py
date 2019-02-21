# File:         hw4_part5.py
# Writting by:  Brandon Nguyen
# Date:         10/6/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter in a string and a single
#               character. The program then counts how many times the character
#               appears in the string and prints out the amount of occurences.
#               This program is not case sensitive.

def main():

    string = str(input("Please enter a string: "))
    stringL = string.lower()
    char = input("Please enter a char: ")
    charL = char.lower()
    instances = stringL.count(charL)

    print("The character '" , char, "' appears ", instances, " times in the string: \n \t'", string, "'")
    
main()
