class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")

class Marks(Student):
    def __init__(self, student_id, name, algo, dataScience, Calculus):
        super().__init__(student_id, name)
        self.marks_algo = algo
        self.marks_dataScience = dataScience
        self.marks_calculus = Calculus

    def display_marks(self):
        print(f"Marks in Algorithm: {self.marks_algo}")
        print(f"Marks in Data Science: {self.marks_dataScience}")
        print(f"Marks in Calculus: {self.marks_calculus}")

class Result(Marks):
    def total_marks(self):
        return self.marks_algo + self.marks_dataScience + self.marks_calculus

    def average_marks(self):
        return self.total_marks() / 3

    def display_result(self):
        self.display_info()
        self.display_marks()
        print(f"Total Marks: {self.total_marks()}")
        print(f"Average Marks: {self.average_marks()}")


result = Result(student_id="S001", name="John Doe", algo=85, dataScience=90, Calculus=80)
result.display_result()
