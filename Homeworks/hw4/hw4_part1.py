# File:         hw4_part1.py
# Writting by:  Brandon Nguyen
# Date:         10/4/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter the height of a triangle
#               and what symbol the triangle will be made of. Then, it prints
#               the triangle with the given height and symbol.


def main():
    
    height = int(input("Please enter the height of your triangle: "))
    char = input("Please enter the single character for the symbol: ")
    level = 1

    for counter in range(height):
        temp = ""
        for i in range(level):
            temp += char
        print(temp)
        level+=1

main()
