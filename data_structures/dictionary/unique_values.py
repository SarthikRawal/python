# 7. Write a Python program to print all unique values in a dictionary.

def unique_values(dict):
    unique_vals = set()
    for d in dict:
        for value in d.values():
            unique_vals.add(value)
    return unique_vals

if __name__ == '__main__':
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                   {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    result = unique_values(sample_data)
    print("Unique Values:", result)
