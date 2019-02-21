# File:         hw3_part2.py
# Written by:   Brandon Nguyen
# Date:         9/24/15
# Lab Section:  20
# UMBC email:   brando15@umbc.edu
# Description:  This program is a grade calculator and prompts the user to
#               enter in 6 values. Assuming that the user enters in valid
#               values, the program will calculate the user's grade.

def main() :
    hwWeight = float(input("Please enter the homework weight: "))
    hwGrade = float(input("Please enter the homework grade: "))
    examWeight = float(input("Please enter the exam weight: "))
    examGrade = float(input("Please enter the exam grade: "))
    dWeight = float(input("Please enter the discussion weight: "))
    dGrade = float(input("Please enter the discussion grade: "))

    hw = hwGrade * hwWeight
    exam = examWeight * examGrade
    discussion = dWeight * dGrade
    total = hw + exam + discussion

    print ("The final numerical grade is : ", total)

    if total <= 100 and total >= 90:
        print("This earns you an A in the class.")
    elif total <= 89.9 and total >= 80:
        print("This earns you a B in the class.")
    elif total <= 79.9 and total >= 70:
        print("This earns you a C in the class.")
    elif total <= 69.9 and total >= 60:
        print("This earns you an D in the class.")
    elif total <=59.9:
        print("This earns you an E in the class.")

main()
