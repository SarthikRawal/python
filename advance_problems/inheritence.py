# Inheritance
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

class ParentClass:
    def __init__(self):
        self.parent_attribute = "I am a parent class attribute"

    def parent_method(self):
        print("This is a parent class method")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.child_attribute = "I am a child class attribute"

    def child_method(self):
        print("This is a child class method")

obj = ChildClass()
print(obj.parent_attribute)  # Accessing parent class attribute
obj.parent_method()          # Accessing parent class method
print(obj.child_attribute)   # Accessing child class attribute
obj.child_method()           # Accessing child class method
