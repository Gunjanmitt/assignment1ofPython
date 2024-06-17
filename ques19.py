def remove_punctuation(input_string):
    punctuation_marks='''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    result_string=""
    for char in input_string:
        if char not in punctuation_marks:
            result_string+=char
    return result_string       
input_string = "Hello, World! This is a test string, with some punctuation."
print("Original string:", input_string)
print("String without punctuation:", remove_punctuation(input_string)) 


    