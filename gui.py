from tkinter import *
import elevhanterare

# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/


skola = elevhanterare.ElevHanterare()


# create a root window.
root = Tk()
root.title("Skolan")

# create listbox object
listbox = Listbox(root, height = 60,
                  width = 100,
                  bg = "white",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "blue")

 
# Define the size of the window.
root.geometry("1000x800") 
 
# create a label
label_elevnamn = Label(root, text="Elevens namn:")
label_elevnamn.grid(row=0, column=0, sticky=E, padx=5, pady=5)

# create an input textbox
textbox_elevnamn = Entry(root)
textbox_elevnamn.grid(row=0, column=1, sticky=W, padx=5, pady=5)

label_elev_tel = Label(root, text="Unikt TelNr: ")
label_elev_tel.grid(row=1, column=0, sticky=E, padx=5, pady=5)
textbox_tel = Entry(root)
textbox_tel.grid(row=1, column=1, sticky=W, padx=5, pady=5)

label_elev_prog = Label(root, text="Program: ")
label_elev_prog.grid(row=2, column=0, sticky=E, padx=5, pady=5)
textbox_prog = Entry(root)
textbox_prog.grid(row=2, column=1, sticky=W, padx=5, pady=5)


def clickSparaButton():
    #print("butt spara click" + textbox_elevnamn.get())
    elever = skola.add_elev(textbox_elevnamn.get(), textbox_prog.get(), textbox_tel.get())
    #Tömmer Entrys dvs textboxar
    textbox_elevnamn.delete(0, END)
    textbox_tel.delete(0, END)
    textbox_prog.delete(0, END)
    #sätter focus på första entry
    textbox_elevnamn.focus_set()
    update_listBox(elever)


def clickTabortButton():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        value = listbox.get(index)
        elever = skola.del_elev(index)
        update_listBox(elever)
        print(f"Selected item: {value} och index = {index}")
    else:
        print("No item selected")  

button_spara = Button(text="spara", command = clickSparaButton)
button_spara.grid(row=3, column=0, sticky=E, padx=15, pady=15)

button_del = Button(root,text="Ta bort", command=clickTabortButton)
button_del.grid(row=3, column=1, sticky=W, padx=15, pady=15)

listbox.grid(row=4, column=0, columnspan=2)
#button = Button(root, text="Get selection", command=get_selection)

def update_listBox(t_elevlista):

    #tömmer listbox
    listbox.delete(0, END)
    # insert elements by their
    # index and names.
    i = 1
   
    for item_elev in t_elevlista:
        listbox.insert(i, item_elev.namn+ ", Tel: " +item_elev.tel+ ", Utbildning: " + item_elev.utbildning)
        #listbox.insert(2, "Sandwich")
        
        i+=1


update_listBox(skola.get_elevlist())
# pack the widgets
#label.pack()
#listbox.pack()
 
 
# Display until User
# exits themselves.
root.mainloop()