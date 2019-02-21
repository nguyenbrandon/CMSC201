# File:         hw6_part1.py
# Written by:   Brandon Nguyen
# Date:         10/20/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program asks the user to continuously enter in names until
#               they enter in "DONE". After all the names are entered, the 
#               progam says hello to every name entered
#


def main():
    end = ""
    names = []
    myFile = open("names.txt" , 'w')
    while end!= "DONE":
        end = input("Please enter a name (or \"DONE\" to stop): ")
        if end!= "DONE":
            names.append(end)
    for i in range(len(names)):
        myFile.write("Hello "+ names[i] + "!\n")
    myFile.close()
main()

