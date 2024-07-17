# Employee Wages
import random

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
WORKING_DAYS_PER_MONTH = 20

def check_attendance():
    """
    check for employee attendance status
    """
    return random.randint(0, 2)

def daily_wage(emp_type):
    """
    calculate daily and part time wage 
    """
    match emp_type:
        case 0:
            return "Absent..!"
        case 1: 
            return WAGE_PER_HOUR * FULL_DAY_HOURS
        case 2:
            return WAGE_PER_HOUR * PART_TIME_HOURS
         