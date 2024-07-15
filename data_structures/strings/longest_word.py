# 5. Write a Python function that takes a list of words and returns the length of the longest one.

def longest_words(words):
    max_length = 0
    for word in words:
        if max_length > len(word):
            max_length = len(word)
    return word

if __name__ == '__main__':
    words = ['apple', 'banana', 'kiwi', 'pineapple']
    print("longest word: ", longest_words(words))