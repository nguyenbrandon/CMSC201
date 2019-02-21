# File:         hw4_part2.py
# Writting by:  Brandon Nguyen
# Date:         10/4/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter a width and height of a
#               box and a symbol. The program then creates a box with the
#               given measurements and symbol. Only the edges of the box are 
#               made out of the symbol and the area of the box is blank.

def main():

    width = int(input("Please enter the width of your box: "))
    height = int(input("please enter the height of your box: "))
    char = input("please enter a single character for the symbol: ")
    spot = 0

    for counter in range(height):
        if spot == 0 or spot == height-1:
            for i in range (width):
                print(char, end = "")
            print('\n', end = "")
        
        else:
            print(char, end = "")
            for i in range (width - 2):
                print(" ", end = "")
            print(char, end = "")
            print('\n', end = "")
        spot += 1

main()
