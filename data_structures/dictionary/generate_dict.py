# 5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

if __name__ == '__main__':
    n = 5
    result = generate_dict(n)
    print("Generated Dictionary:", result)
    