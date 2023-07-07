from FClass import Fan
from FCuserdisplay import FCUSerDisplay

class TestFan:
    def __init__(self):
        self.first_fan = self.assign_fan("First Fan: ")
        self.second_fan = self.assign_fan("Second Fan: ")
        self.Fan = Fan()
        self.FCUD = FCUSerDisplay()