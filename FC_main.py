from FClass import Fan

# Write a test program named TestFan that creates two fan objects. For the first object, assign a maximum speed, radius 10, color yellow, and turn it on.
class TestFan:
    def __init__(self):
        self.Fan = Fan()
    input(\
    """
    What do you want to change?
    1 = speed
    2 = radius
    3 = color

    Your choice: 
    """)
    
# Assign medium speed, radius 5, color blue, and turn it off for the second object.
# Display each object's speed, radius, color, and on properties.