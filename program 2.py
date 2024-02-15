numbers = []

for i in range(10):
    value = float(input(f"Enter value {i+1}: "))
    numbers.append(value)

largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"The largest number is: {largest_number}")
