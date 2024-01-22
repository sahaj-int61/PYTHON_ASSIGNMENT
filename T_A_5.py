"""
Write a program to print below patterns.
Date: 21/12/23
""" 
   # Asking the user to enter a number to decide the number of lines for the pattern
n = int(input("Enter your number: "))

# Loop to print the first pattern
for i in range(n):
   # Printing 'n - i' spaces and then 'i + 1' '*' symbols in each line
   print(' ' * (n - i) + '* ' * (i + 1))

# Loop to print the second pattern
for i in range(n-1, -1, -1):
   # Printing 'n - i' spaces and then 'i + 1' '*' symbols in each line
   print(' ' * (n - i) + '* ' * (i + 1))