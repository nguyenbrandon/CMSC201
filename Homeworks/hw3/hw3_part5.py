# File:         hw3_part5.py
# Written by:   Brandon Nguyen
# Date:         9/24/15
# Lab Section:  20
# UMBC email:   brando15@umbc.edu
# Description:  The purpose of this program is to prompt the user to enter the
#               day of the month. Assuming the month starts on a Monday, the
#               program then determines which day of the week it is. If the 
#               user enters an invalid number, the program says so.

def main() :

    day = int(input("Please enter the day of the month: "))
    
    if day == 1 or day == 8 or day == 15 or day == 22 or day == 29 :
        print("Today is a Monday!")
        
    elif day == 2 or day == 9 or day == 16 or day == 23 or day == 30 :
        print("Today is a Tuesday!")
            
    elif day == 3 or day == 10 or day == 17 or day == 24 or day == 31 :
        print("Today is a Wednesday!")
                
    elif day == 4 or day == 11 or day == 18 or day == 25 :
        print("Today is a Thursday!")

    elif day == 5 or day == 12 or day == 19 or day == 26 :
        print("Today is a Friday!")

    elif day == 6 or day == 13 or day == 20 or day == 27 :
        print("Today is a saturday!")

    elif day == 7 or day == 14 or day == 21 or day == 28 :
        print("Today is a Sunday!")
    
    else :
        print("Invalid day.")

main()
