dictionary={"Alice":85,"James":90,"Sam":70,"Sara":89,"Mike":99}
name = input("Enter the student's name: ")
if name in dictionary:
    print(f"{name}'s marks: ",dictionary.get(name))
else:
    print("Student not found.")