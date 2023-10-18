
class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        self.subjects = []

    def add_subject(self, subject, marks):
        self.subjects.append((subject, marks))

    def calculate_average_marks(self):
        total_marks = sum(marks for _, marks in self.subjects)
        return total_marks / len(self.subjects)

student1 = Student(1, "Satoru Gojo")
student2 = Student(2, "Mori Sukuna")

student1.add_subject("EM", 90)
student1.add_subject("FDS", 85)
student1.add_subject("SE", 78)

student2.add_subject("EM", 88)
student2.add_subject("FDS", 92)
student2.add_subject("SE", 80)

print(f"Student 1 - Roll Number: {student1.roll_number}, Name: {student1.name}")
print("Subjects and Marks:")
for subject, marks in student1.subjects:
    print(f"{subject}: {marks}")
print(f"Average Marks: {student1.calculate_average_marks()}")

print("\n")

print(f"Student 2 - Roll Number: {student2.roll_number}, Name: {student2.name}")
print("Subjects and Marks:")
for subject, marks in student2.subjects:
    print(f"{subject}: {marks}")
print(f"Average Marks: {student2.calculate_average_marks()}")
