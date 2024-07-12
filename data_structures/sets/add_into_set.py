# 3. Write a Python program to add member(s) in a set.

cars = {"Tata", "BMW", "Porche", "Toyota"}

# adding single items
cars.add("Tesla")
print("-->", cars)

# adding multiple items
new_data = ["Mahindra", "McLaren"]
cars.update(new_data)
print("-->", cars)
