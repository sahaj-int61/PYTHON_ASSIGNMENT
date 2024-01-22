"""
Write a program to find two string Anagram or Not.
Date: 21/12/23
"""
def sort_word(word):
    """
    This function used for sorting operation.
    params:
        word:str
    returns:
        sorted_word:str
    """
    # Convert the word to a list of characters
    word_list = list(word)

    # Implement a simple sorting algorithm
    for _ in range(len(word_list)):
        for j in range(0, len(word_list) - 1):
            if word_list[j] > word_list[j + 1]:
                print(word_list)
                # Swap characters if they are in the wrong order
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
                print(word_list)
    # Join the sorted characters back into a string
    return ''.join(word_list)

def are_anagrams(word1, word2):

    # Sort the letters in both words
    sorted_word1 = sort_word(word1)
    sorted_word2 = sort_word(word2)


    # Check if the sorted words are the same
    if sorted_word1 == sorted_word2:    
        return True
    else:
        return False

# Get input from the user for two words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
# Check if the two words are anagrams using the are_anagrams() function
if are_anagrams(word1, word2):
    print("The two words are anagrams.")
else:
    print("The two words are not anagrams.")