from FClass import Fan
class TestFan:
    def __init__(self):
        self.first_fan = self.assign_fan("First Fan: ")
        self.second_fan = self.assign_fan("Second Fan: ")
        self.Fan_display()
    
    def assign_fan(self):
        print("Assign Fan object: ")
        input(\
        """
        What properties do you want in your fan?
        
        SPEED:
        1 = SLOW
        2 = MEDIUM
        3 = FAST

        RADIUS:
        1-10

        COLOR (can be anything you want):
        """)
        