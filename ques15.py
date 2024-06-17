import csv

# Name of the CSV file
csv_file = 'data.csv'

# Reading data from the CSV file
with open('C:/Users/mehak/OneDrive/Desktop/assignment1/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
