student_data = []

def add_student():
    roll_number = input("Enter student roll number: ")
    name = input("Enter student name: ")
    sub1 = float(input("Enter marks for subject 1: "))
    sub2 = float(input("Enter marks for subject 2: "))
    sub3 = float(input("Enter marks for subject 3: "))
    student_tuple = (roll_number, name, (sub1, sub2, sub3))
    student_data.append(student_tuple)

def display_student_by_name():
    search_name = input("Enter the name of the student to search for: ")
    found = False
    for student_tuple in student_data:
        if student_tuple[1] == search_name:
            print(f"Roll Number: {student_tuple[0]}")
            print(f"Marks: {student_tuple[2]}")
            found = True
    if not found:
        print(f"No student with the name '{search_name}' found.")

def sort_student_data_by_name():
    sorted_data = sorted(student_data, key=lambda x: x[1])
    for student_tuple in sorted_data:
        print(f"Roll Number: {student_tuple[0]}")
        print(f"Name: {student_tuple[1]}")
        print(f"Marks: {student_tuple[2]}")
        print()

while True:
    print("\nMenu:")
    print("1. Add Student Data")
    print("2. Display Student Data by Name")
    print("3. Sort Student Data by Name")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_student_by_name()
    elif choice == '3':
        sort_student_data_by_name()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
