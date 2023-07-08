class Pet:
    def __init__(self):
        self.__name = None
        self.__animal_type = None 
        self.__age = None

    def setName(self, name):
        self.__name = name

    def setAnimal_type(self, animal_type):
        self.__animal_type = animal_type

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name
    
    def getAnimal_type(self):
        return self.__animal_type
    
    def getAge(self):
        return self.__age