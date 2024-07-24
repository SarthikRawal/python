# Encapsulation
# Encapsulation involves bundling the data and the methods that operate on the data within a single unit or class, and restricting access to some of the object's components.

class EncapsulatedClass:
    def __init__(self, value):
        self._hidden_value = value  # protected variable

    def get_value(self):
        return self._hidden_value

    def set_value(self, value):
        self._hidden_value = value


obj = EncapsulatedClass(10)
print(obj.get_value())  # Accessing through getter method
obj.set_value(20)       # Modifying through setter method
print(obj.get_value())
