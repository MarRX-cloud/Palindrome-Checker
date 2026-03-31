class palindrome_checker:
    def __init__(self, entered_string):
        self.entered_string = entered_string  # encapsulate the input string within the class
 
    def setString(self, entered_string):
        self.entered_string = entered_string  # optional setter
 
    def getString(self):
        return self.entered_string  # optional getter
 
    def is_palindrome(self):
        '''# Example: "Racecar" should return True.
        # length of the string is 7
        # length // 2 is 3, this is because integer division rounds down
        # index: 0 1 2 3 4 5 6
        # string: r a c e c a r
        # when i = 0: 7 - 0 - 1 = 6 → r == r
        # when i = 1: 7 - 1 - 1 = 5 → a == a
        # we use length - i - 1 to compare characters from start and end
        '''
        cleaned_string = "".join(self.entered_string.split()).lower()  # remove spaces, lowercase
        length = len(cleaned_string)
 
        for i in range(length // 2):
            if cleaned_string[i] != cleaned_string[length - i - 1]:
                return False  # Return False if any characters do not match
        return True  # Return True if all characters match
 
#   Main program  
entered_string = input("Enter a string: ")  # Prompt user for input
checker = palindrome_checker(entered_string)  # create object
print("Is it a palindrome?:", checker.is_palindrome())  # call method
