from FClass import Fan

class FCUSerDisplay(Fan):
    def assign_fan(self):
        print("Assign Fan object: ")

        on = input("Is the fan on? ")

        speed = int(input(\
        """
        What speed properties do you want in your fan?
        
        SPEED:
        1 = SLOW
        2 = MEDIUM
        3 = FAST
        """))
        
        radius = float(input(\
        """
        RADIUS:
        1-10
        """))

        color = input("COLOR (can be anything you want): ")

        fan = Fan(on, speed, radius, color)
        return fan
    