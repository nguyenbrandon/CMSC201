# File:         hw3_part3.py
# Written by:   Brandon Nguyen
# Date:         9/24/15
# Lab Section:  20
# UMBC email:   brando15@umbc.edu
# Description:  This program is meant to be a medical diagnosis software.
#               As a programmer, I am only allowed to ask the user 2-3 
#               questions. First, I ask if the user has a fever and depending
#               on the user's response, I ask a series of follow up questions.
#               Depending on the user's answers, their diagnosis is calculated
#               and printed at the end of the program.

def main() :
    fever = input("Do you have a fever? (y/n) ")

    if fever == "y" :
        rash = input("Do you have a rash? (y/n) ")
        
        if rash == "y":
            print("Your diagnosis: You have the Measles.")
        elif rash == "n":
            ear = input("Does your ear hurt? (y/n) ")
        
            if ear == "y" :
                print("Your diagnosis: You have an Ear Infection.")
            elif ear == "n" :
                print("Your diagnosis: You have the flu.")
                
    elif fever == "n" :
                
        nose = input("Do you have a stuffy nose? (y/n) ")
                
        if nose == "y" :
            print("Your diagnosis: You have a head cold.")
        elif nose == "n" :
            print("Your diagnosis: You are a hypochondriac.")
                    
main()
