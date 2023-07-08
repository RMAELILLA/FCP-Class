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

    def savePetinfo():
        pet = Pet()
        pet.setName(name_entry.get())
        pet.setAnimal_type(Animal_type_entry.get())
        pet.setAge(age_entry.get())
        userdisplay(pet)
    
    save_button =  Button(root, text="Save", command=savePetinfo)

    