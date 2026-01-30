class Student:
    def __init__(self, citizen_id, name, age, student_id):
        self.citizen_id = citizen_id
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"{self.student_id}: {self.name} ({self.age} years old)"
