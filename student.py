from person import Person

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student[PID={self.pid}, Name={self.name}, Age={self.age}, StudentID={self.student_id}]"