from collections import defaultdict

def split_by_first_character(words_list):
    # Using defaultdict to automatically handle missing keys
    split_dict = defaultdict(list)
    
    for word in words_list:
        first_char = word[0]
        split_dict[first_char].append(word)
    
    return dict(split_dict)


if __name__ == '__main__':
    words_list = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'avocado', 'carrot']
    split_dict = split_by_first_character(words_list)

    print("Split dictionary:")
    for key, value in split_dict.items():
        print(f"{key}: {value}")
