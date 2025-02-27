#Store employee names and salaries in a dictionary:

employees = {}
while True:
    name = input("Enter employee name (or 'exit' to stop): ")
    if name == 'exit':
        break
    salary = int(input("Enter salary: "))
    employees[name] = salary
print("Employee data:", employees)
