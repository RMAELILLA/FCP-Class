class FCUSerDisplay:
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
        