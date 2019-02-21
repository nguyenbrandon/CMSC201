# File:         hw4_part4.py
# Writting by:  Brandon Nguyen
# Date:         10/6/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program prints the numbers from 1-100(inclusive). However,
#               there are 3 instances where we would not print the number. If
#               the number is not divisible by 5 and is divisible by 3, then it
#               prints a quote. If the number is not divisible by 3 and is 
#               divisible by 5, then it prints a different quote. Finally, if 
#               the number is divisible by both 3 and 5, then it prints another
#               unique quote.

def main():

    for i in range(1,101):
        if i%3 == 0 and i%5 != 0:
            print("Better three hours too soon that a minute too late.")
        
        elif i%3 != 0 and i%5 == 0:
            print("Where do you see yourself in five years?")
        
        elif i%3 == 0 and i%5 == 0:
            print("In the future, everyone will be world-famous for 15 minutes.")
        else:
            print(i)

main()
