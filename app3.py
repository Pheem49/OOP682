from model.student import Student
from model.classroom import ClassRoom

oop = ClassRoom("OOP")
oop.add_student(Student(1234567890123, "Alice", 20, "S123"))
oop.add_student(Student(2345678901234, "Bob", 22, "S456"))

print(f'{oop.name} registers {len(oop)} students:')

oop.add_student(Student(3456789012345, "Charlie", 21, "S789"))
print(len(oop))

print("students in the class:")
for i in range(len(oop)):
    print(oop[i])
