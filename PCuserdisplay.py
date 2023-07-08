
def userdisplay():
    name = input("Enter the pet's name: ")
    animal_type = input("Enter the pet's type: ")
    age = input("Enter the pet's age: ")
    return name, animal_type, age

def userPetinfo(pet):
    print("Pet's Name:", pet.getName())
    print("Pet's Type:", pet.getAnimal_type())
    print("Pet's Age:", pet.getAge())
# Write a program that creates an object of the class and prompts the user to enter the name, type, age of his or her pet.
# This data should be stored as the object's attributes.
# Use the object's accessor methods to retrieve the pet's name, type, and age and display this data on the screen.