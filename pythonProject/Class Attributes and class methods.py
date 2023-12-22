# class Person:
#     type = "Person"
#     description = "Describes a person"
#
#
# print(Person.type)  # Person
# print(Person.description)  # Describes a person
#
# Person.type = "Class Person"
# print(Person.type)  # Class Person




################################################################


# class Person:
#     type = "Person"
#
#     def __init__(self, name):
#         self.name = name
#
#
# tom = Person("Tom")
# bob = Person("Bob")
# print(tom.type)  # Person
# print(bob.type)  # Person
#
# # Change the attribute of the class
# Person.type = "Class Person"
# print(tom.type)  # Class Person
# print(bob.type)  # Class Person

################################################################

# class Person:
#     default_name = "Undefined"
#
#     def __init__(self, name):
#         if name:
#             self.name = name
#         else:
#             self.name = Person.default_name
#
#
# tom = Person("Tom")
# bob = Person("")
# print(tom.name)  # Tom
# print(bob.name)  # Undefined
################################################################
# class Person:
#     name = "Undefined"
#
#     def print_name(self):
#         print(self.name)
#
#
# tom = Person()
# bob = Person()
# tom.print_name()  # Undefined
# bob.print_name()  # Undefined
#
# bob.name = "Bob"
# bob.print_name()  # Bob
# tom.print_name()  # Undefined

################################################################

# tom = Person()
# bob = Person()
# tom.print_name()    # Undefined
# bob.print_name()    # Undefined


################################################################

# bob.name = "Bob"
# bob.print_name()    # Bob
# tom.print_name()    # Undefined


#################################################################
# tom = Person()
# bob = Person()
# tom.print_name()  # Undefined
# bob.print_name()  # Undefined
#
# Person.name = "Some Person"  # change the value of the class attribute
# bob.name = "Bob"  # set the attribute of the object
# bob.print_name()  # Bob
# tom.print_name()  # Some Person

################################################################


# class Person:
#     __type = "Person"
#
#     @staticmethod
#     def print_type():
#         print(Person.__type)
#
#
# Person.print_type()  # Person - invoking a static method via the class name
#
# tom = Person()
# tom.print_type()  # Person - accessing a static method via object name

################################################################
