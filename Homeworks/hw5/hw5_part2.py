# File:         hw5_part2.py
# Written by:   Brandon Nguyen
# Date:         10/10/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter two integers; a width
#               and height. The program then prints a box using the given 
#               dimensions & the box is made out of numbers counting up from 1.


def main():

    width = int(input("Please enter a width: "))
    height = int(input("Please enter a height: "))
    counter = 1
    for i in range (height):
        for i in range (width):
            print (counter ,"",  end = "")
            counter+=1
        print("\n", end = "")

main()
