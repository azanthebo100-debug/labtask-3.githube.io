numbers = []
even = 0
odd = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

print("\nSum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)
