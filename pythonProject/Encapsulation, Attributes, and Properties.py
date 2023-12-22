# class Person:
#     def __init__(self, name):
#         self.name = name  # defining the name
#         self.age = 1  # set the age
#
#     def display_info(self):
#         print(f"Name: {self.name}\tAge: {self.age}")
#
#
# tom = Person("Tom")
# tom.name = "Spider-Man"  # change the name attribute
# tom.age = -129  # change the age attribute
# tom.display_info()  # Name: Spider-Man Age: -129
##############################################################################

# class Person:
#     def __init__(self, name):
#         self.__name = name  # set the name
#         self.__age = 1  # set the age
#
#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print("Invalid age")
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Name: {self.__name}\tAge: {self.__age}")
#
#
# tom = Person("Tom")
# tom.display_info()  # Name: Tom Age: 1
# tom.set_age(-3486)  # Age invalid
# tom.set_age(25)
# tom.display_info()  # Name: Tom Age: 25

##############################################################################
# def get_age(self):
#     return self.__age

##############################################################################
# def set_age(self, age):
#     if 1 < age < 110:
#         self.__age = age
#     else:
#         print("Invalid age")

##############################################################################

class Person:
    def __init__(self, name):
        self.__name = name  # set the name
        self.__age = 1  # set the age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Invalid age")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}\tAge: {self.__age}")


tom = Person("Tom")

tom.display_info()  # Name: Tom Age: 1
tom.age = -3486  # Invalid age
print(tom.age)  # 1
tom.age = 36
tom.display_info()  # Name: Tom Age: 36

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

