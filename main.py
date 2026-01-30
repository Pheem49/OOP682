class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

class staff:
    def __init__(self, pid, name, age, staff_id):
        self.pid = pid
        self.name = name
        self.age = age
        self.staff_id = staff_id

class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id


student = Student(1234567890123, "Alice", 20, "S123")

staff = Staff(2345678901234, "Bob", 35, "ST456")

print(f"Student: {student.name}, Age: {student.age}, Student ID: {student.student_id}")

print(f"Staff: {staff.name}, Age: {staff.age}, Staff ID: {staff.staff_id}")

def get_person_info(person):
    print(get_person_info(student))
    return f"Name: {person.name}, Age: {person.age}"




