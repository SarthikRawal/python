# 5. Write a Python program to remove an item from a set if it is present in the set.

def remove_if_present(set, data):
    if data in set:
        set.remove(data)
        return set
    else:
        return "item not found"

if __name__ == '__main__':
    cars = {'BMW', 'Mahindra', 'Porche', 'McLaren'}
    result = remove_if_present(cars, 'Porc')
    print("-->",result)