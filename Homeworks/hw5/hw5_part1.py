# File:         hw5_part1.py
# Written by:   Brandon Nguyen
# Date:         10/10/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter a number between 0 and
#               100, inclusive. If the user enters an invalid number, the 
#               program will keep asking for a number until it is valid.

def main():
    num = -1
    while num < 0 or num > 100:
        num = int(input("Please enter a number (between 0 and 100, inclusive): "))
        if num >=0 and num <=100:
            print("Thank you for selecting the number ", num)
        else:
            print("That is an invalid number, please try again.")


main()
