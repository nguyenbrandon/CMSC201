#factorial(n) computes the factorial of a number n
#the factorial of a number n is defined as:
#    factorial(n) = n * (n-1) * (n-2) * ... * 2 * 1
#
def factorial(n):
    product = n
    for x in range(2,n):
        product = product * (x)
    return product


#no errors below this line
def main():

    print("Should print: 120\nPrints: ",end="")
    print(factorial(5))

main()
