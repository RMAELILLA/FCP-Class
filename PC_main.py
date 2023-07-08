from tkinter import Tk, Label, Entry, Button
from PClass import Pet
from PCuserdisplay import userPetinfo

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
        userPetinfo(pet)
    
    save_button = Button(root, text="Save", command=savePetinfo)

    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    Animal_type_label.grid(row=1, column=0)
    Animal_type_entry.grid(row=1, column=1)
    age_level.grid(row=2, column=0)
    age_entry.grid(row=2, column=1)
    save_button.grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    GUI()