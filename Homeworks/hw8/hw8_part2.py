#File:         hw8_part2.py
#Author:       Brandon Nguyen
#Date:         11/24/15
#Section:      20
#E-mail:       Brando15@umbc.edu
#Description:  This program asks the user for a symbol and the height
#              of a triangle. Using the recursive function tri(), the
#              program prints out an upside-down triangle (tip down)
#              using the symbol and height given.

def tri(height, char):
    for i in range(0,height):
        print(char, end = "")
    print()

    if height == 0:
        return 0
    else:
        tri(height - 1, char)
        return height




def main():
    height = int(input("Please enter the height of your triangle: "))
    char = input("Please enter a character for your triangle: ")
    print()
    tri(height, char)
    


main()
