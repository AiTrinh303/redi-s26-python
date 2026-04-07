class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getName(self):
        return self.name

    def printGrade(self):
        print(f"{self.name}'s grade is: {self.grade}")

student1 = Student("Ai", 9.5)
print(student1.getName())  # Output: Ai
student1.printGrade()      # Output: Ai's grade is: 9.5