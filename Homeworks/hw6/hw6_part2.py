# File:         hw6_part2.py
# Written by:   Brandon Nguyen
# Date:         10/20/15
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program first asks the user to enter in a file name to
#               read. The program then reads the file and calculates the 
#               weighted grade by using the grades given in the file.

def main():
    grade = 0
    gradesList = []
    fileName = input("Please enter the name of the file that contains the grades: ")
    myGrades = open(fileName, 'r')
    for line in myGrades:
        line = line.strip()
        line = line.split()
        gradesList.append(line)

    
    for i in range(len(gradesList)):
        sum = 0
        average = 0
        counter = 0
        total = 0
        for l in range(len(gradesList[i])):
            weight = float(gradesList[i][0])
            if l>0:
                sum = sum + int(gradesList [i][l])
                counter +=1
        average = sum / counter
        total = average * weight
        grade = grade + total
    print("Your final weighted score is" , grade)
    
    myGrades.close()
main()
