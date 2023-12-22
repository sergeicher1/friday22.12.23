class Person:
    __type = "Person"

    def __init__(self, name):
        self.name = name  # name of the Person

    def name(self):
        return self.name

    def DisplayInfo(self):
        print(f"Name: {self.name}")





class Employee(Person):

    def Work(self):
        print(f"{self.name()} works")


class Student(Employee):

    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    # def Studies(self):
    #     print(f"{self.name()} studies")

    def DisplayInfo(self):
        super().DisplayInfo()
        print(f"Studies at: {self.school}")


tom = Student("tom", "MEGO")
tom.DisplayInfo()
