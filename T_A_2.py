"""
Write a program to swap comma and dot in string.
Date: 21/12/23
"""
def swapfunc(i):
    """
    Swap commas and dots in a string.
    Args:
        string (str): Input string with commas and dots.
    Returns:
        str: String with commas and dots swapped.
    """
    swap = i.maketrans(',.','.,')
    print(swap)
    numbers = i.translate(swap)
    return numbers

# Example usage:
number = input("Enter number with comma and dot: ")
new_number = swapfunc(number)
print(new_number)

# i = 12,36,26.6
# num = i.maketrans(',.','.,')
# print(num)

