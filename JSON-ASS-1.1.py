import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
with open('employee.json') as f:
    data = json.load(f)
employees_data = data['employees']
employees = []
for emp_data in employees_data:
    emp = Employee(emp_data['Name'], emp_data['DOB'], emp_data['Height'], emp_data['City'], emp_data['State'])
    employees.append(emp)
for emp in employees:
    print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")


                
