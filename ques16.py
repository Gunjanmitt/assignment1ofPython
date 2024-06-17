def count_characters(input_string):
    char_frequency={}
    for char in input_string:
        if char in char_frequency:
            char_frequency[char]+=1
        else:
            char_frequency[char]=1
    return char_frequency            
input_string=input("enter a string:")
frequency_dict = count_characters(input_string)

for char, frequency in frequency_dict.items():
    print(f"Character '{char}' occurs {frequency} times.")
