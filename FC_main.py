from FClass import Fan
from FCuserdisplay import FCUSerDisplay

class TestFan:
    def __init__(self):
        self.first_fan = self.FCUD.assign_fan("First Fan: ")
        self.second_fan = self.FCUD.assign_fan("Second Fan: ")
        self.Fan = Fan()
        self.FCUD = FCUSerDisplay()
    def fan_properties(self):
        print("First Fan: ")
        self.fan_properties(self.first_fan)

        print("\nSecond Fan: ")
        self.fan_properties(self.second_fan)
        