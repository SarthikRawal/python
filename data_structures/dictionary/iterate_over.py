# 4. Write a Python program to iterate over dictionaries using for loops.

def iterate_over_dict(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':        
    my_dict = {
        "car1": "Volvo",
        "car2": "Kia",
        "car3": "BMW",
        "car4": "Tata",
    }

    iterate_over_dict(my_dict)
