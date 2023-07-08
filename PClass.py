# Write a class named Pet, which should have the following data attributes:
class Pet:
    def __init__(self):
# __name (for the name of the pet)
        self.__name = None
# __animan_type (for the type of animal that a pet is. Example values are 'Dog', 'Cat', and 'Bird')
        self.__animal_type = None 
# __age (for the pet's age)
        self.__age = None
# The pet class should have an __init__ method that creates these attributes. It should also have the following methods:

# setName() # This method assigns a value to the __name field.
    def setName(self, name):
        self.__name = name

# setAnimal_type() # This method assigns a value to the __animal_type field.
    def setAnimal_type(self, animal_type):
        self.__animal_type = animal_type

# setAge # This method assigns a value to the __age field.
    def setAge(self, age):
        self.__age = age

# getName() # This method returns the value of the __name field.
    def getName(self):
        return self.__name
    
# getAnimal_type() # This method returns the value of the __animal_type field.
    def getAnimal_type(self):
        return self.__animal_type
    
# getAge() # This method returns the value of the __age field.
    def getAge(self):
        return self.__age
# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, age of his or her pet.
# This data should be stored as the object's attributes.
# Use the object's accessor methods to retrieve the pet's name, type, and age and display this data on the screen.