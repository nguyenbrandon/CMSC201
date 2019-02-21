#File:           password.py
#Author:         Brandon Nguyen
#Date:           10/07/15
#Section:        20
#E-mail:         brando15@umbc.edu
#Description:    This program asks the user to enter a password. If the user 
#                guesses incorrectly three times, the program locks them out.

def main():


    password = "jaimeewilllose"
    counter = 3
    guess = ""

    while guess != password and counter > 0:
        guess = input("Please enter your password: ")
        counter -= 1
        
        if guess!= password and counter != 0:
            print("WRONG. You have", counter, "guesses left.")

    if guess == password:
        print("Access granted!")
    elif guess != password:
        print("Access denied, too many incorrect guesses.")
        
main()
