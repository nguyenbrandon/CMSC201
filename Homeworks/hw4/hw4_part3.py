# File:         hw4_part3.py
# Writting by:  Brandon Nguyen
# Date:         10/6/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter 10 subjects and stores 
#               them into a list. Then, if the string ends in "ology" then the 
#               user is able to "study" the subject. Otherwise, the program
#               prints the string back out to the user.


def main():

    suffix = "ology"
    wordList = []

    for i in range (0,10):
        wordList.append(input("Please enter a word: "))
        
    for i in range (0,10):
        if wordList[i].endswith(suffix) == 1:
            print("You can study", wordList[i])
        
        else:
            print(wordList[i])


main()
