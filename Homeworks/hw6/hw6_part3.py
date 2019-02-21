# File:         hw6_part3.py
# Written by:   Brandon Nguyen
# Date:         10/21/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program asks the user to enter in the file name that they
#               would like to read. If the file name is invalid (doesn't end in
#               .txt or .dat) then the program keeps asking the user for a name
#               until the input is valid. The program then prints out the total
#               amount of words and characters in the file.


def main():
    wordList = []
    fileName = "hooplah"

    while fileName.endswith(".dat")== 0 and fileName.endswith(".txt")== 0:

        fileName = input("Please enter the name of the file to open: ")
        if fileName.endswith(".dat")==0 and fileName.endswith(".txt") ==0:
            print("\tThe file must end in .txt or .dat to be valid.")
    
    
    textFile = open(fileName, 'r')

    for line in textFile:
        line = line.strip()
        line = line.split()
        wordList.append(line)
    
    wordTotal = 0
    for i in range(len(wordList)):
        wordTotal += (len(wordList[i]))
    print("The file " + fileName + " has", wordTotal, "words in it.")


    charCounter = 0
    for word in wordList:
        for letter in word:
            for robbie in letter:
                charCounter += 1

    characterAvg = charCounter / wordTotal
    
    print("On average, each word is", characterAvg, "characters long.")
    textFile.close()

main()
