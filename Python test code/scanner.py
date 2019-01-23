from tkinter import *

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text = "Enter Password:")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.password = Entry(self)
        self.password.grid(row =0, column = 1 , sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row = 1, column = 1,columnspan = 2, sticky = W)


        self.text = Text(self,width=35,height=5,wrap=WORD)
        self.text.grid(row = 3,column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        content = self.password.get()

        if content == "MRTadmin":
            message = "Welcome to Device Manager!"

        elif content == "":
            message = "Enter a password..."


        else:
            message = "Acceess Denied."

        self.text.delete(0.0, END)
        self.text.insert(0.0, message)


def func(event):
    print("You hit return.")
root.bind('<Return>', func)

def onclick():
    print("You clicked the button")

button = tk.Button(root, text="click me", command=onclick)
button.pack()

root = Tk()
root.title("Login")
root.geometry("250x150")
app = Application(root)
root.mainloop()