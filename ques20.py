def calculate_sum(numbers):
    total=0

    for num in numbers:
        total+=num
    return total
numbers=[1,2,3,4,5]
print("the list of numbers:",numbers)
print("Sum of the numbers:", calculate_sum(numbers))