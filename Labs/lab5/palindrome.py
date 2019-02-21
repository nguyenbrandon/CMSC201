#File:        palindrome.py
#Author:      Brandon Nguyen
#Date:        9/30/15
#Section:     20
#E-mail:      brando15@umbc.edu
#Description: The program prompts the user to enter a string and the program
#             checks to see if the string is a palindrome

def main():

    word = input("Please enter a string: ")
    word2 = ""
    for i in range (len(word)-1,-1,-1):
        word2 = word2 + word[i]

    if word == word2:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")





main()
