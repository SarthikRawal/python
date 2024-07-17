# Employee Wages
import random

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
WORKING_DAYS_PER_MONTH = 20
MAX_WORKING_HOURS = 100

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
            return 0,0 #Absent
        case 1: 
            return WAGE_PER_HOUR * FULL_DAY_HOURS, FULL_DAY_HOURS
        case 2:
            return WAGE_PER_HOUR * PART_TIME_HOURS, PART_TIME_HOURS
         
def monthly_wage():
    total_wages = 0
    total_hours = 0
    total_days = 0
    attendance = check_attendance()
    while total_days < WORKING_DAYS_PER_MONTH and total_hours < MAX_WORKING_HOURS:
        wage, hours = daily_wage(attendance)
        
        total_wages += wage
        total_hours += hours
        total_days += 1

    return total_wages, total_hours, total_days

def main():
    total_wage, total_hours, total_days = monthly_wage()
    print(f"Total wage: {total_wage}💰")
    print(f"Total hours worked: {total_hours}")
    print(f"Total days worked: {total_days}")

if __name__ == "__main__":
    main()