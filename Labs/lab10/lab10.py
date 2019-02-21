#File name:    lab10.py
#Author:       Brandon Nguyen
#Date:         11/4/15
#Section:      20
#E-mail:       brando15@umbc.edu
#Description:  This program asks the user of they would like to encrypt a string or decrypt a string. Then the program asks the user how much they want to shift the string. After encrypting/decrypting the given string, the program prints it out.




def encrypt(n):
    string = input("Enter plain text message: ")
    encryption = []
    for char in range(len(string)):
        encryption.append(ord(string[char]))
        encryption[char] += n
        if encryption [char] >90:
            encryption[char] -= 26
            
    print("Your encrypted message is : ", end = "")
    for char in range(len(encryption)):
            print(chr(encryption[char]), end = "")
    print()

def decrypt(n):
    string = input("Enter encrypted message: ")
    decryption = []
    for char in range(len(string)):
        decryption.append(ord(string[char]))
        decryption[char] -= n
        if decryption[char] < 65:
            decryption[char] += 26
    print("Your plain text message is: ", end = "")
    for char in range(len(decryption)):
        print(chr(decryption[char]), end = "")
    print()





def main():

    print("What would you like to do?")
    print("1. Encrypt String")
    print("2. Decrypt String")
    option = int(input("Enter 1 or 2: "))
    n = int(input("How much would you like to shift? (1-26): "))
    if option == 1:
        encrypt(n)
    if option == 2:
        decrypt(n)

main()
