def is_palindrome(s): # Function to check if the given string is a palindrome
    cleaned_string = "".join(s.split()).lower() # Used to remove any spaces and converts the given string to lowercase
    length = len(cleaned_string) # grabs the length of the cleaned string
 
    for i in range(length // 2): # Loops through half of the cleaned string
        if cleaned_string[i] != cleaned_string[length - i - 1]: # Compares the characters from the start and end moving towards the center
            return False # If characters dont match it reutrns false.
    return True # Otherwise it returns true.

entered_string = input("Enter a string: ") # Prompts the user to enter a string
print("Is it a palindrome?:", is_palindrome(entered_string)) # Calls the function and prints out the results.