file_path='textfile2.txt'

try:
    with open("C:/Users/mehak/OneDrive/Desktop/assignment1/textfile2.txt",'r')as file:
        file_content=file.read()
        print("the file content is:",file_content)
except FileNotFoundError:
    print("file not found")