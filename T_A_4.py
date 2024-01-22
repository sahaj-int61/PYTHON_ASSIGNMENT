"""
Write a program to reverse middle words of string.
Date: 21/12/23
"""

def reverse_middle_words(string):
    words = string.split()  #print(words) Split the input string into words  
    n = len(words)

    if n <= 2:
        return string
    else:
        for i in range(1, len(words) - 1):
            words[i] = words[i][::-1]
        return ' '.join(words) # Join the words back into a string  # (words[1:-1] = [w[::-1] for w in words[1:-1]])  Reverse the middle words (use for loop)

# Test the function
string = input("Enter the string: ") # Input string
print("The original string is: ",string) # Output the original string
print("The string with reversed middle word is: ",reverse_middle_words(string)) # Output the string with reversed middle words