# Create a class - Student. Use the method concept, 
# to fetch student name and marks for them

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getDetails(self):
        print(f"Hi! my name is {self.name},I received {self.marks} marks.")

    def getDetails1(self):
        print(f"Hi! my name is {self.name},I received {self.marks} marks.")

stud1=Student("Suresh",89)
stud2=Student("Ramesh",95)

stud1.getDetails()
stud2.getDetails1()