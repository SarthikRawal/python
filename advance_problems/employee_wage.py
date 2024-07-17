# Employee Wages
import random

class Employee:

    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4
    WORKING_DAYS_PER_MONTH = 25
    MAX_WORKING_HOURS = 100

    def __init__(self, name, wage_per_hr):
        self.emp_name = name
        self.wage_per_hr = wage_per_hr
        self.total_hrs_worked = 0
        self.total_days_worked = 0
        self.total_wage = 0        
    
    @staticmethod    
    def check_attendance():
        """
        check for employee attendance status
        """
        return random.randint(0, 2)
    
    def daily_wage(self):
        """
        calculate daily and part time wage 
        """
        emp_status = self.check_attendance()
        match emp_status:
            case 0:
                return 0,0 #Absent
            case 1: 
                return self.wage_per_hr * self.FULL_DAY_HOURS, self.FULL_DAY_HOURS
            case 2:
                return self.wage_per_hr * self.PART_TIME_HOURS, self.PART_TIME_HOURS
            
    def monthly_wage(self):
        while self.total_days_worked < self.WORKING_DAYS_PER_MONTH and self.total_hrs_worked < self.MAX_WORKING_HOURS:
            wage, hours = self.daily_wage()
            
            self.total_wage += wage
            self.total_hrs_worked += hours
            self.total_days_worked += 1

    def get_emp_salary_details(self):
        print(f"Total Wage: {self.total_wage}") 
        print(f"Total Hours Worked: {self.total_hrs_worked}")
        print(f"Total Days Workde: {self.total_days_worked}")


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation")

    emp = Employee("sarthik", 20)
    # daily_wage = emp.daily_wage()
    emp.monthly_wage()
    emp.get_emp_salary_details()