def count_occurences(lst,element):
    count=0
    for item in lst:
        if item==element:
            count+=1
    return count
my_list = [1, 2, 2, 3, 4, 2, 5, 2]
element_to_count = 2
print("Occurrences of", element_to_count, "in the list:", count_occurences(my_list, element_to_count))        