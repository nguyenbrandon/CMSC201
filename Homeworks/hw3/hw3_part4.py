# File:         hw3_part4.py
# Written by:   Brandon Nguyen
# Date:         9/24/15
# Lab Section:  20
# UMBC email:   brando15@umbc.edu
# Description:  This program asks the user about the current state of two 
#               switches. If both are set to the same setting, then the
#               generator is off. If both are set to opposite settings, then
#               the generator is on.

def main() :

    switch1 = input("Is the first switch on? (y/n) ")
    switch2 = input("Is the second switch on? (y/n) ")
    
    if switch1 == switch2 :
        print("The generator is off.")
        
    else :
        print("The generator is on.")

main()
