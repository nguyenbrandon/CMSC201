# File:         hw2.py
# Writting by:  Brandon Nguyen
# Date:         9/14/15 
# Lab section:  20
# UMBC Email:   brando15@umbc.edu
# Description:  This program demonstrates my ability to perform order of
#               operation correctly in python


# Question 1
# Expected Output: 24
num1 = (7+1)*3
print ("Number 1 evaluates to:", num1)
# Actual Output: 24
# Explanation: parenthesis first (8), then multiplication (24)


# Question 2
# Expected Output: 2
num2 = ( 12 % 5 )
print ("Number 2 evaluates to:", num2)
# Actual Output: 2
# Explanation: 12/5 is 2 remainder 2


# Question 3
# Expected Output: 21
num3 = (21%49)
print ("Number 3 evaluates to:", num3)
# Actual Output: 21
# Explanation: 21/49 is 0 remainder 21


# Question 4
# Expected Output: 2
num4 = (5-3) + (10-5) * (8%2)
print ("Number 4 evaluates to:", num4)
# Actual Output: 2
# Explanation: parenthesis first (2 + 5 * 0), then multiplication (2+0),
#              then addition (2)


# Question 5
# Expected Output: 34 
num5 = 6.5 + 5 / 2 * (4+7)
print ("Number 5 evaluates to:", num5)
# Actual Output: 34
# Explanation: parenthesis first (6.5 + 5/2 * 11), then division and
#              multiplication (6.5 + 27.5), then addition (34)


# Question 6
# Expected Output: 5
num6 = 9 / 3 + 18 - 4 * 4
print ("Number 6 evaluates to:", num6)
# Actual Output: 5
# Explanation: multiplication first, then division (3 + 18 - 16), then addition
#              (21 - 16), then subtraction (5)

# Question 7
# Expected Output: 22
num7 = 8 % 3 + 5 * 4
print ("Number 7 evaluates to:", num7)
# Actual Output: 22
# Explanation: modulo and multiplication first (2 + 20), then addition (22)

# Question 8
# Expected Output: 79.9143
num8 = 81.3 / 2.1 + ((51.5 % 65.2) * 2 / 2.5)
print ("Number 8 evaluates to:", num8)
# Actual Output: 79.9143
# Explanation: modulo first, then multiplication, then division, then addition


# Question 9 
# Given equation: 100 - 8 * 8 + 1 / 0.5
# Solved equation:
# Target number: -30
num9 = 100 - ((8 * 8) + 1) / 0.5
print ("Number 9 evaluates to:", num9, "and should be -30")


# Question 10
# Given equation:   84 / 10 + 11 - 4 * 4
# Solved equation:  (84/ (10+11) - 4) * 4
# Target number :   0
num10 = (84 / (10 + 11) - 4) * 4
print ("Number 10 evaluates to:", num10, "and should be 0")
