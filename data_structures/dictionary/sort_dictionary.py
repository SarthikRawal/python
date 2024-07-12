# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

def sort_dictionary(dictionary):
    # ascending order
    sort_asce = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    # desecnding order
    sort_desc = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse = True))

    return sort_asce, sort_desc

if __name__ == '__main__':
  
    example_dict = {
        "apple": 3,
        "mango": 2,
        "orange": 4,
        "lemon": 1,
    }

    sorted_asc, sorted_desc = sort_dictionary(example_dict)
    print("Ascending", sorted_asc)
    print("descending", sorted_desc)