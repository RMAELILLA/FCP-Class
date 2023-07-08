from FClass import Fan

class FCUSerDisplay(Fan):
    def assign_fan(self, fan_name):
        print(f"Assign object properties {fan_name}")

        on = input("Is the fan on? ").lower() == "yes"

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

        color = input(\
        """
        COLOR (can be anything you want): 
        """)

        fan = Fan(on, speed, radius, color)
        return fan