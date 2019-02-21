# File:             dealership.py
# Author:           Brandon Nguyen
# Date:             10/21/15
# Section:          20
# E-mail:           brando15@umbc.edu
# Description:      This program goes through a list of cars and checks to see
#                   which cars are red with 4 doors and cost less than 30,000

def main():

    carFile = open("cars.txt", 'r')
    results = open("results.txt", 'w')
    for line in carFile:
        carName , color, doors, cupH, price = line.split(",")
        if color == "red" and doors == "4" and float(price) < 30000:
            results.write(carName + " --- $" + price)
    carFile.close()
    results.close()

main()
