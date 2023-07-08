from Cclass import Car

class Cmain:
    def userdisplay():
        year_model = input("Enter the year model of the car: ")
        make = input("Enter the make of the car: ")
    
        car = Car(year_model, make)

        for _ in range (5):
            car.accelerate()
            print("Current Speed: ", car.get_speed())
        
        for _ in range(5):
            car.brake()
            print("Current speed: ", car.get_speed())

Cmain.userdisplay()