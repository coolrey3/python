from tkinter import *
from tkinter import ttk
root = Tk()
label = ttk.Label(root, text = "Mobile Repair Techs Device Manager")
label.grid(column =0,)
label.config(justify = LEFT)
label.config(foreground = 'white', background = 'black')
label.config(font = "Courier",)
logo = PhotoImage(file = 'I:/Projects\Mobile Repair Techs/MRT Media/Mobile repair tech logo files/final_vector_logo.gif')
label.img = logo
label.config(image=label.img)


root.title('MRT Device Manager | Log In')
label.config(compound = 'left')

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text = "Enter Username:")
        self.instruction.grid(row = 0, column = 1, columnspan = 1, sticky = E)

        self.username = Entry(self)
        self.username.grid(row =0, column = 2 , sticky = W)

        self.instruction = Label(self, text = "Enter Password:")
        self.instruction.grid(row = 1, column = 1, columnspan = 1, sticky = E)

        self.password = Entry(self)
        self.password.grid(row =1, column = 2 , sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row = 1, column = 2,columnspan = 2, padx = 1)

        self.text = Text(self,height=1,wrap=WORD,)
        self.text.grid(row = 3,column = 1, columnspan = 2, sticky = W,)

    def reveal(self):
        uncontent=self.username.get()
        content=self.password.get()

        if content == "C00lb3ans1" and uncontent == "MRTadmin":
            message = "Welcome to Device Manager!"

        elif content == "":
            message = "Enter a password..."
            

        else:
            message = "Acceess Denied."

        self.text.delete(0.0,END)
        self.text.insert(0.0, message,)

#def callback():

#root = Tk()
#root.title("Login")
#root.geometry("250x150")
app = Application(root)

root.mainloop()
