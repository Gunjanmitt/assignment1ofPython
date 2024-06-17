def copy_file(source_file, destination_file):
    try:
        with open("C:/Users/mehak/OneDrive/Desktop/assignment1/textfile3.txt", 'r') as f_source, open("C:/Users/mehak/OneDrive/Desktop/assignment1/textfile4.txt", 'w') as f_dest:
            f_dest.write(f_source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage:
source_file = 'textfile3.txt'            # Replace with your source file path
destination_file = 'textfile4.txt'  # Replace with your destination file path

copy_file(source_file, destination_file)
