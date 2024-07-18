
class Employee:

    working_hrs = 100

    def __init__(self, name) -> None:
        self.emp_name = name

    def get_emp_name(self):
        return self.emp_name
    
    @classmethod
    def set_wrk_hrs(cls, hrs):
        cls.working_hrs = hrs
        return cls('x')
    
    @staticmethod
    def demo():
        print("static method")


emp = Employee("Sarthik")
print(emp.get_emp_name())
Employee.demo()
