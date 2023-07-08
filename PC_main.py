from tkinter import Tk, Label, Entry, Button
from PClass import Pet
from PCuserdisplay import userdisplay, userPetinfo

def GUI():
    root = Tk()
    root.title("Pet Information")

    name_label = Label(root, text="Name: ")
    name_entry = Entry(root)
    Animal_type_label = Label(root, text="Animal Type: ")
    Animal_type_entry = Entry(root)
    age_level = Label(root, text="Age: ")
    age_entry = Entry(root)

def main():
    pet = Pet()

    name, animal_type, age = userdisplay()

    pet.setName(name)
    pet.setAnimal_type(animal_type)
    pet.setAge(age)

    userPetinfo(pet)

if __name__ == "__main__":
    main()