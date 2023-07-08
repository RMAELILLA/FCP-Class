from CC_userdisplay import CCUD

class Cmain:
    def userdisplay(self):
        year_model = input("Enter the year model of the car: ")
        make = input("Enter the make of the car: ")
    
        car = Car(year_model, make)