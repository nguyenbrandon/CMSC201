# File:         hw3_part1.py
# Writting by:  Brandon Nguyen
# Date:         9/24/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program takes in three numbers from the user 
#               and finds the average

def main():

    num1 = float(input("Please enter a floating point number: "))

    num2 = float(input("Please enter a floating point number: "))

    num3 = float(input("Please enter a floating point number: "))

    average = ((num1 + num2 + num3) / 3 )

    print("The average of the three floats is: ", average)

main()
