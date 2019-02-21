




class Ong:

    def __init__(self, word):
        self.word = word

    def isVowel(self, letter):
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            return True
        return False

    def translateOng(self):
        for letter in self.word:
            print(letter, end = "")
            if self.isVowel(letter) == False:
                print("ong", end = "")


def main():
    
    string = input("Enter a string to translate: ")
    word = Ong(string)
    word.translateOng()
    print()
main()
