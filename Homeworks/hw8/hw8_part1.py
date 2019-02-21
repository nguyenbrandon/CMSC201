#File:         hw8_part1.py
#Author:       Brandon Nguyen
#Date:         11/24/15
#Section:      20
#E-mail:       Brando15@umbc.edu
#Description:  This program takes in a list of numbers from the user.
#              Then, by using the recursive funtion rev(), the program
#              prints out all of the contents of the list in its 
#              reversed order.

#NOTE: Worked with Ellen Gupta




def rev(index, numList):
    
    if index == 0:
        print(numList[0])
        return 0
    else:
        print(numList[index])
        index -= 1
        return rev(index, numList)

def main():
    numList = []
    num = 0
    while num != -1:
        num = int(input("Enter a number to append to the list, or -1 to stop: "))
        if num != -1:
            numList.append(num)

    print("The list as you entered it is:", numList)
    print("The reversed list is: ")
    rev(len(numList)-1, numList)

main()
