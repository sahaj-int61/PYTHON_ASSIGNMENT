"""
Write a program to find the ASCII value of each character of the string in python.
Date: 21/12/23
"""

# Declare a string
string = input("Enter your string: ")

# Iterate through each character in the string
for char in string:
    # Use the ord() function to get the ASCII value of the character
    ascii_value = ord(char)
    
    # Print the character and its ASCII value
    print(char,"-", ascii_value, end=",")