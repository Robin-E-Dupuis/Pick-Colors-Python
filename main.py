from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()

    window.config(bg=color[1])


def clickk():
    color = colorchooser.askcolor()

    button.config(bg=color[1])
    button2.config(bg=color[1])
    button3.config(bg=color[1])
def clickkk():
    color = colorchooser.askcolor()

    button.config(fg=color[1])
    button2.config(fg=color[1])
    button3.config(fg=color[1])

window = Tk()
window.geometry("420x420")

button = Button(text="Pick your Background Color", command=click)
button2 = Button(text="Pick your buttons color", command=clickk)
button3 = Button(text="Pick your Text color", command=clickkk)

button.pack()
button2.pack()
button3.pack()
window.mainloop()