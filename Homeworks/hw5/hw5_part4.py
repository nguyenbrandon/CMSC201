# File:         hw5_part4.py
# Written by:   Brandon Nguyen
# Date:         10/10/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program asks the user to enter in numbers until they enter
#               the word "end". Those numbers are stored into list1. The
#               program asks the user to do the same thing again except the
#               numbers are stored into list2. The program then creates a third
#               list named list3 and it contains the values of list1 and list2
#               added together. The program then prints list3 at the end.


def main():

    num = ""
    list1 = []
    list2 = []
    
    while num != "end" and num!= "End" :
        num = input("Please enter a number (or 'end' to stop): ")   
        if num != "end" and num!= "End" :
            number = int(num)
            list1.append(number)
    print("Thank you for completing the first list.")
    
    num2 = ""
    while num2 != "end" and num2!= "End" :
        num2 = input("Please enter a number (or 'end' to stop): ")   
        if num2 != "end" and num2!= "End" :
            number2 = int(num2)
            list2.append(number2)
    print("Thank you for completing the second list.")


    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    
    print(list3)

main()
