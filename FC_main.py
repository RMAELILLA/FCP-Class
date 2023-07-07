from FClass import Fan
from FCuserdisplay import FCUSerDisplay

class TestFan:
    def __init__(self):
        self.FCUD = FCUSerDisplay()
        self.first_fan = self.FCUD.assign_fan("First Fan: ")
        self.second_fan = self.FCUD.assign_fan("Second Fan: ")
    def fan_properties(self):
        print("First Fan: ")
        self.fan_properties(self.first_fan)

        print("\nSecond Fan: ")
        self.fan_properties(self.second_fan)
    def fan_object(self, fan):
        print("ON: ", fan.fanOn())
        print("Speed: ", fan.getSpeed())
        print("Radius: ", fan.getRadius())
        print("Color", fan.getColor())

test = TestFan()
test.fan_properties()