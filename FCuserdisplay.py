class FCUSerDisplay:
    def assign_fan(self):
        print("Assign Fan object: ")
        
        speed = (input(\
        """
        What speed properties do you want in your fan?
        
        SPEED:
        1 = SLOW
        2 = MEDIUM
        3 = FAST
        """))
        
        radius = input(\
        """
        RADIUS:
        1-10
        """)

        color = input("COLOR (can be anything you want): ")

        on = input("Is the fan on? ")

        fan = Fan(on, speed, radius, color)
        return fan