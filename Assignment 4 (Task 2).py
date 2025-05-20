str1=input("Enter text to write to the file: ")
with open ('output.txt','w') as file1:
    writing_file1=file1.write(str1)
print("Data successfully written in output.txt")
str2=input("\nEnter additional text to append: ")
with open ('output.txt','a') as file1:
    writing_file2=file1.write("\n"+ str2)
print("Data successfully appended.")
print("\n Final content of output.txt: ")
with open ('output.txt','r') as file1:
    reading_file=file1.read()
    print(reading_file)