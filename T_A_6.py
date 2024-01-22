"""
Write a program which can accept a number and return the nearest palindrome number.
Date: 21/12/23
""" 
def test(n):

    result = 0
    while n:
        # check if n minus the current result is a palindrome
        print(str(n-result))
        print(str(n+result))
        if str(n-result)==str(n-result)[::-1]:
            return n-result
        # check if n plus the current result is a palindrome
            
        elif str(n+result)==str(n+result)[::-1]:
            return n+result
        # increment the result
        result+=1

n = int(input("Enter a number: ")) #123000
print("Closest Palindrome number of the said number: ",test(n)) # learn