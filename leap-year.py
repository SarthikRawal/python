# 2. Leap Year

def calculate_leap_year(year):
    if(len(str(year)) != 4 ):
        return "Enter a valid year"
    if((year % 4) == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
    
year = int(input("Enter a year: "))

print(calculate_leap_year(year))