# File:         hw5_part3.py
# Written by:   Brandon Nguyen
# Date:         10/10/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prompts the user to enter the starting height of
#               the hailstone. The program does not end until the height = 1.
#               If the height is even, it is divided by 2. If it is odd, the
#               height is multiplied by 3, then added by 1. The height is 
#               displayed after every change. 

def main():

    height = int(input("Please input the starting height of the hailstone: "))
    
    while height != 1:
        if height % 2 == 0:
            height = height//2
        else:
            height = (height*3) + 1
        print("Hail is currently at height ", height)



main()
