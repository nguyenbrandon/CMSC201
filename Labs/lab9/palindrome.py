#tests whether myString is a palindrome
def isPalindrome(myString):
    tempString = myString
    length = len(tempString)
    half = length/2
    isPalindrome=True
    for i in range(int(half)):
        if myString[i] != myString[(length-1)-i]:
            isPalindrome = False
    print(isPalindrome)
#no errors below this line
def main():
    print("Should print: True\nPrints: ",end="")
    isPalindrome("tacocat")
    print("Should print: False\nPrints:", end="")
    isPalindrome("pineapple")
main()
