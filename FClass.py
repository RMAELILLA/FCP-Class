class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self,  on = False, speed = SLOW, radius = 5, color = "blue"):
        self.__on = on
        self.__speed = speed
        self.__radius = radius
        self.__color = color
 
    def fanOn(self):
        return self.__on
    def setOn(self, on):
        self.on = on
    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        self.__speed = speed
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color