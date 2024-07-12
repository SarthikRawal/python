# 8. Write a Python program to find the list of words that are longer than n from a given list of words.

def find_words(list, n):
    new_list = []
    for items in list:
        if len(items) > n:
            new_list.append(items)
    return new_list

if __name__ == '__main__':
    my_list = ["BMW", "Mahindra", "Tata", "Toyota", "Nissan"]
    print(find_words(my_list, 4))