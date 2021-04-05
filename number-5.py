# A class that takes atleast two methods
# gets a string from the user input
# converts it in uppercase


class Strings:

    def __init__(self):
        pass
    
    def getString(self):
        self.word = input("Enter a string : \n")
    
    def printString(self):
        print(self.word.upper())

s = Strings()
s.getString()
s.printString()
    