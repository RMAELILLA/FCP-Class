
def userdisplay():
    name = input("Enter the pet's name: ")
    animal_type = input("Enter the pet's type: ")
    age = input("Enter the pet's age: ")
    return name, animal_type, age

def userPetinfo(pet):
    print("Pet's Name:", pet.getName())
    print("Pet's Type:", pet.getAnimal_type())
    print("Pet's Age:", pet.getAge())