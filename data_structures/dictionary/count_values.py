# 10. Write a Python program to count the values associated with key in a dictionary. 
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
# False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

def count_the_value(dict):
    count = 0
    for i in dict:
        if i.get('success') == True:
            count += 1
    return count 

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'success': True, 'name': 'Lary'}, 
        {'id': 2, 'success': False, 'name': 'Rabi'}, 
        {'id': 3, 'success': True, 'name': 'Alex'}
    ]
    result = count_the_value(sample_data)
    print(result)