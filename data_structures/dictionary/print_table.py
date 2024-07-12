# 9. Write a Python program to print a dictionary in table format.

def print_dict_table(d):
    print("{:<10} {:<10}".format('Key', 'Value'))
    print("----------------")
    for key, value in d.items():
        print("{:<10} {:<10}".format(key, value))

if __name__ == '__main__':
    sample_dict = {"apple": 10, "banana": 20, "kiwi": 30}
    print_dict_table(sample_dict)