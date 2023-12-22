# class subclass (Super Class):
#     subclass_methods


###############################################################################


# class Person:
#
#     def __init__(self, name):
#         self.__name = name  # person's name
#
#
# @property
# def name(self):
#     return self.__name
#
#
# def display_info(self):
#     print(f"Name: {self.__name} ")

###############################################################################

# class Employee:
#
#     def __init__(self, name):
#         self.__name = name  # employee's name
#
#
# @property
# def name(self):
#     return self.__name
#
#
# def display_info(self):
#     print(f"Name: {self.__name} ")
#
#
# def work(self):
#     print(f"{self.name} works")

###############################################################################

# class Person:
#
#     def __init__(self, name):
#         self.__name = name  # person's name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Name: {self.__name} ")
#
#
# class Employee(Person):
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# tom = Employee("Tom")
# print(tom.name)  # tom
# tom.display_info()  # Name: Tom
# tom.work()  # Tom works

###############################################################################

# print(tom.name) # tom
# tom.display_info()  # Name: Tom


###############################################################################
# def work(self):
#     print(f"{self.__name} works")   # ! Error


###############################################################################
# Worker class


# class Employee:
#     def work(self):
#         print("Employee works")
#
#
# # Student Class
# class Student:
#     def study(self):
#         print("Student studies")
#
#
# class WorkingStudent(Employee, Student):  # Inheritance from Employee and Student classes
#     pass
#
#
# # Working Student Class
# tom = WorkingStudent()
# tom.work()  # Employee works
# tom.study()  # Student studies

###############################################################################

# class Employee:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# class Student:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def study(self):
#         print(f"{self.name} studies")
#
#
# class WorkingStudent(Employee, Student):
#     pass
#
#
# tom = WorkingStudent("Tom")
# tom.work()  # Tom works
# tom.study()  # Tom studies

###############################################################################


###############################################################################



###############################################################################


###############################################################################




