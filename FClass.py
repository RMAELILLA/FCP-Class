# Design a class named Fan to represent a fan. The class contains:
class Fan:
# Three constant named SLOW, MEDIUM, and FAST, with the values 1,2, and 3 to denote the fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self,  on = False, speed = SLOW, radius = 5, color = "blue"):
        self.__on = on
        self.__speed = speed
        self.__radius = radius
        self.__color = color

#checked    # A private data field named speed that specifies whether the fan is on (the default is False)
            # A private float data field named radius that specifies the radius of the fan
            # A private string data field named color that specifies the color of the fan

# The accessor (getters) and mutator(setters) methods for all four data fields.
    def fanOn(self):
        return self.__on
    def setOn(self, on):
        self.on = on

# A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False)

# Write a test program named TestFan that creates two fan objects. For the first object, assign a maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object's speed, radius, color, and on properties.