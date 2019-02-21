#File:           store.py
#Author:         Brandon Nguyen
#Date:           10/14/15
#Section:        20
#E-mail:         brando15@umbc.edu
#Description:    This program displays a shop's inventory and the cost of each item. The program then asks the user what they would like to buy with $100.
#                After each item selection, their budget is decreased by the item's cost. The program keeps asking the user what they would like to buy
#                until the user enters 0.
def main(): 

    items = ["shoes", "socks", "hat", "belt", "blouse", "dress", "tie"]
    prices = [54.99, 7.11, 6.49, 22.58, 21.73, 38.99, 14.83]
    budget = float(100)
    selection = 1


    while selection!= 0:
        print("You have $", budget, "in funds available")
        for i in range(len(items)):
            print( i+1 , "-" , items[i] , "\t$ " , prices[i])
        selection = int(input("Please choose an item # to purchase, or '0' to quit: "))
        if(budget >= prices[selection-1] and selection!=0):
            print("Thank you for purchasing" , items[selection-1])
            budget = budget - prices[selection-1]
            
        else:
            print("Sorry but you are unable to afford that item.")

        print("\n", end = "")

    print("Thank you for shopping at Python Mart!")
    print("You have $", budget, "in funds available")
    print("Thank you for coming!")

main()
