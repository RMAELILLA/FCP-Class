from PClass import Pet
from PCuserdisplay import userdisplay, userPetinfo

def main():
    pet = Pet()

    name, animal_type, age = userdisplay()

    pet.setName(name)
    pet.setAnimal_type(animal_type)
    pet.setAge(age)

    userPetinfo(pet)

if __name__ == "__main__":
    main()