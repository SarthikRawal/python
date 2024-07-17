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
        print(f"Name: {self.emp_name}")
        print(f"Total Wage: {self.total_wage}") 
        print(f"Total Hours Worked: {self.total_hrs_worked}")
        print(f"Total Days Workde: {self.total_days_worked}")


class Company:
    def __init__(self, name) -> None:
        self.company_name = name
        self.employee_dict = {}

    def add_employee(self, emp_obj: Employee):
        self.employee_dict.update({emp_obj.emp_name: emp_obj})

    def delete_employee(self, emp_obj: Employee):
        self.employee_dict.pop(emp_obj.emp_name)
    
    def display_emp_detail(self):
        # print(self.employee_dict)
        for emp in self.employee_dict.values():
            emp.get_emp_salary_details()
            print("="*30)

class Multiple_Company:
    def __init__(self) -> None:
        # self.company_name = name
        self.company_dict = {}

    def add_company(self, com_obj: Company):
        self.company_dict.update({com_obj.company_name: com_obj})

    def delete_company(self, com_obj: Company):
        self.company_dict.pop(com_obj.company_name)

    def display_company(self):
        print("Companies:")
        for com in self.company_dict.values():
            print(f"Company: {com.company_name}")


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation")

    emp = Employee("sarthik", 20)
    emp.monthly_wage()
    emp1 = Employee("rawal", 30)
    emp1.monthly_wage()
    com = Company("Apple")
    com1 = Company("Google")
    
    companies = Multiple_Company()
    companies.add_company(com)
    companies.add_company(com1)
    companies.display_company()
    print("="*30)
    com.add_employee(emp)
    com.add_employee(emp1)
    com.display_emp_detail()

    # com.delete_employee(emp1)
    # com.display_emp_detail()
