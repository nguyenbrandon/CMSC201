#File:         hw8_part3.py
#Author:       Brandon Nguyen
#Date:         11/24/15
#Section:      20
#E-mail:       Brando15@umbc.edu
#Description:  This program takes in two integers (greater than 0) 
#              from the user and calculates the greatest common
#              denominator of the two numbers by calling a recursive
#              function named gcd().

#NOTE: Worked with Ellen Gupta

def gcd(num1, num2, index):

    if num1 % index == 0 and num2 % index == 0:
        return index
    else:
        return gcd(num1, num2, index - 1)


def main():
    
    num1 = 0
    while num1 <= 0:
        num1 = int(input("Please enter the first integer: "))
        if num1 <= 0:
            print("Your number must be positive (greater than 0).")


    num2 = 0
    while num2 <= 0:
        num2 = int(input("Please enter the second integer: "))
        if num2 <= 0:
            print("Your number must be positive (greater than 0).")
    
    if num1 > num2:
        index = num2
    else:
        index = num1

    GCD = gcd(num1, num2, index)
    print("The GCD of", num1, "and", num2, "is", GCD)
    print()

main()
