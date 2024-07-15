# 6. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

def upper_lower_case(str):
    upper, lower = str.upper(), str.lower()
    return upper, lower

input = input("Enter a string:")
upper_case, lower_case = upper_lower_case(input)

print("Upper Case:", upper_case)
print("Lower Case:", lower_case)