# File:        temperature.py
# Author:      Brandon Nguyen
# Date:        9/23/15
# Section:     20 
# E-mail:      brando15@umbc.edu
# Description: to take in the temperature and display an output depending on
#              the temperature


degrees = int(input("Please enter a temperature in Fahrenheit: "))


if degrees < 25:
    print("It's freezing outside.")

elif degrees > 24 and degrees < 50:
    print("It's a bit chilly, remember to bundle up.")

elif degrees > 49 and degrees < 80:
    print("The weather is wonderful!")

elif degrees > 79 and degrees < 101:
    print("It's pretty hot outside")

elif degrees > 100:
    print("It is way too hot.")


