def find_min_max(numbers):
    if not numbers:
        return None,None
    minimum=min(numbers)
    maximum=max(numbers)

    return minimum,maximum
 
numbers=[1,2,3,4,5,6,8,9,44,33,22,46]
min_value, max_value = find_min_max(numbers)
print("List of numbers:", numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

