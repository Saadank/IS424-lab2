employee_data = {}

while True:
    name = input("Enter employee name (or 'no' to exit): ")

    if name.lower() == 'no':
        break

    salary = float(input("Enter employee salary: "))
    employee_data[name] = salary

print("Employee data:")
for name, salary in employee_data.items():
    print(f"{name}: ${salary}")