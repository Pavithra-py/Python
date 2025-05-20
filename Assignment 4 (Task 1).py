
try:
    with open('sample.txt', 'r') as file1:
        reading_file = file1.read()
        print("Reading the contents of the file:")
        print(reading_file)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
