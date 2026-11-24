try:
    with open("students.txt", "r") as file:
        print("Existing student names:")
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")

n = int(input("How many student names do you want to add? "))

with open("students.txt", "a") as file:
    for i in range(n):
        name = input("Enter student name: ")
        file.write(name + "\n")

with open("students.txt", "r") as file:
    print("\nStudent names:")
    print(file.read())
