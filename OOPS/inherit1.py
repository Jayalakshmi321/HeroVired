class Person(object):

    def __init__(self,name,id): #parameterized constructor
        self.name=name
        self.id=id

    def display(self):
        print(self.name,self.id)

emp=Person("Aditya",100)
emp.display()

class Emp(Person):

    def Print(self):
        print("emp class called")

empDetails=Emp("prabhas",101)
empDetails.Print()
empDetails.display()


