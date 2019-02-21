#File:         hw7.py
#Author:       Brandon Nguyen
#Date:         10/26/15
#Section:      20
#E-mail:       Brando15@umbc.edu
#Description:  This program acts as a calculator that practices the use of
#              functions. After the user enters a list, they can utilize the
#              program to find the minimum value, maximum value, mean, and
#              median of the list.




def getList():
    list = []
    integers = "blah"
    print("Enter a list of integers or 'q' to end the list!")
    while integers!= 'q':
        integers = input("Enter an integer: ")
        if integers != 'q':
           list.append(int(integers))
    return list

def printMenu():
    print("Please choose the statistic you would like to calculate!")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")
    option = int(input("Please enter your choice, or 0 to exit: "))
    return option

def getMean(userList):
    sum = 0
    for number in range(len(userList)):
        sum = sum + userList[number]
    mean = sum / len(userList)
    return mean

def getMedian(userList):
    tempUserList = []
    tempUserList = userList
    tempUserList.sort()
    if len(tempUserList)%2 == 1:
        median = tempUserList[(len(tempUserList)//2)]
    elif len(tempUserList)%2 == 0:
        num1 = tempUserList[len(tempUserList)//2]
        num2 = tempUserList[(len(tempUserList)//2)-1]
        sum = num1 + num2
        median = sum/2
    return median


def getMin(userList):
    min = userList[0]
    for i in range(1,len(userList)):
        if min > userList[i]:
            min = userList[i]
    return min

def getMax(userList):
    max = userList[0]
    for i in range(1,len(userList)):
        if max < userList[i]:
               max = userList[i]
    return max


def emptyList():
    userList = getList()
    return userList


def main():
    print("Welcome to the List Statistics Calculator")
    userList = getList()
    response = 10
    while response != 0:
        response = printMenu()
        if response == 1:
            min = getMin(userList)
            print("The minimum value is:" , min)
        if response == 2:
            max = getMax(userList)
            print("The maximum value is:" , max)
        if response == 3:
            mean = getMean(userList)
            print("The mean value is :" , mean)
        if response == 4:
            median = getMedian(userList)
            print("The median value is :" , median)
        if response == 5:
            userList = emptyList()
    print("Thank you for using our calculator!")


main()
