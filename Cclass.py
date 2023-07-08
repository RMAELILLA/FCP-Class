# Write a class named car that has the following data attributes:
class Car:
    def __init__(self, year_model, make):
# __year_model (for the car's year model)
        self.__year_model = year_model
# __make (for the make of the car)
        self.__make = make
# __speed (for the car's current speed)
        self.__speed = 0

# The car class should have an __init__ method that accepts the car's year model and make as arguments.
# These values should be assigned to the object's __year_model and __make data attributes.
# It should also assign 0 to the __speed data attribute.

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed

# The class should also have the following methods:
# Accelerate() # accelerate method should add 5 from the speed data attribute each time it is called
# Break() # break method should subtract 5 from the speed data attribute each time it is called.
# getSpeed() # The getSpeed method should return the current speed

# Next, desing a program that creates a Car object then calls the accelerate method five times.
# After each call to the accelerate method, get the current speed of the car and display it.
# Then call the brake method five times.
# After each call to the break method, get the current speed of the car and display it. 