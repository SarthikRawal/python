# 7. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def unique_sorted_words(words):
    words_list = words.split(',')
    words_list = [word.strip() for word in words_list]

    unique_words = set(words_list)
    sorted_unique_words = sorted(unique_words)

    result = ', '.join(sorted_unique_words)
    return result

words = 'apple, kiwi, pineapple, banana, orange'
print(unique_sorted_words(words))