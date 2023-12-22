# class class_name:
    # class_attributes
    # class_methods

########################################################################
# class Person:
#     pass
#

########################################################################

# class Person:
#     pass
#
#
# tom = Person()  # definition of tom object
# bob = Person()  # definition of bob object

########################################################################

#
# class Person:  # definition of the Person class
#     def say_hello(self):
#         print("Hello")
#
#
# tom = Person()
# tom.say_hello()  # Hello

########################################################################


# class Person:  # definition of the Person class
#     def say(self, message):  # method
#         print(message)
#
#
# tom = Person()
# tom.say("Hello World")  # Hello World
########################################################################

# self.attribute # Invoking the attribute
# self.method # Invoking the method

########################################################################


# class Person:
#
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say("Hello work")  # refer to the above-defined say method
#
#
# tom = Person()
# tom.say_hello()  # Hello work


########################################################################
# def say_hello(self):
#     say("Hello work")  # ! Error

########################################################################

# class Person:
#     # Constructor
#     def __init__(self):
#         print("Create a Person object")
#
#     def say_hello(self):
#         print("Hello")
#
#
# tom = Person()  # Creating a Person object
# tom.say_hello()  # Hello

########################################################################

# class Person:
#
#     def __init__(self, name):
#         self.name = name  # name of the person
#         self.age = 1  # person's age
#
#
# tom = Person("Tom")
#
# # Accessing Attributes
# # Retrieving Values
# print(tom.name)  # tom
# print(tom.age)  # 1
# # Change the value
# tom.age = 37
# print(tom.age)  # 37

########################################################################
# def __init__(self, name):
#     self.name = name
#     self.age = 1

########################################################################
# print(tom.name)  # get the value of the name attribute
# tom.age = 37  # Change the value of the age attribute

########################################################################

# class Person:
#
#     def __init__(self, name):
#         self.name = name  # name of the person
#         self.age = 1  # person's age
#
#
# tom = Person("Tom")
#
# tom.company = "Microsoft"
# print(tom.company)  # Microsoft

########################################################################
# tom = Person("Tom")
# print(tom.company)  # ! Error - AttributeError: Person object has no attribute company

########################################################################


# class Person:
#
#     def __init__(self, name):
#         self.name = name  # person's name
#         self.age = 1  # person's age
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom")
# tom.display_info()  # Name: Tom  Age: 1

########################################################################

# class Person:
#
#     def __init__(self, name):
#         self.name = name  # name of the person
#         self.age = 1  # person's age
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom")
# tom.age = 37
# tom.display_info()  # Name: Tom  Age: 37
#
# bob = Person("Bob")
# bob.age = 41
# bob.display_info()  # Name: Bob  Age: 41
