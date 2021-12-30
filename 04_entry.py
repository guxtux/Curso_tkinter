from tkinter import *

root = Tk()

e =Entry(root)
e.pack()

def myClick():
    myLabel = Label(root, text="Mira! un botón para presionar!")
    myLabel.pack()

myButton = Button(root, text="Presiona el botón", command=myClick)
myButton.pack()

root.mainloop()