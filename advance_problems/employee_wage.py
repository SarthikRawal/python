# Employee Wages
import random

def check_attendance():
    """
    check for employee attendance status
    """
    return random.randint(0, 1)

def calculate_wage(wage_per_hour = 20, full_day_hour = 8):
    """
    calculate daily wage 
    """
    daily_wage = wage_per_hour * full_day_hour
    return daily_wage