from tkinter import *
from tkinter import ttk
from time import ctime
import datetime
import webbrowser
import xlwt
import xlrd

#Write this to excel file called log ins
wb = xlwt.Workbook()
sheet = wb.add_sheet("Log In TimeStamps")
file = "i:/MRTdevicemanager_logins.xls"

current_time = datetime.datetime.now()
current_time = ctime()

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


        if ((content == "C00lb3ans1" and uncontent == "MRTadmin") or (content == "baker001" and uncontent == "coolrey3")):
            message = "Access Granted: Welcome to Device Manager!"


            #Main Program Starts in New Window after authentication
            
            def create_window():
                window = tk.Toplevel(root)
            def create_window1():
                window1 = tk.Toplevel(root)
            def create_window2():
                window2 = tk.Toplevel(root)
            def create_window3():
                window2 = tk.Toplevel(root)
            def create_window4():
                window2 = tk.Toplevel(root)
            def create_window5():
                window2 = tk.Toplevel(root)

            import tkinter as tk     
            root = tk.Tk()
            label1 = tk.Label(root,text='Invoices').grid(row = 0, column = 0)
            b1 = tk.Button(root, text="Launch", command=create_window)
            b1.grid(column = 1, row = 0)


            #workbook = xlrd.open_workbook(file)

            sheet.write(0,0, (uncontent+ " logged in on %s" % (current_time )))
            wb.save(file)

            print(uncontent+ " logged in on %s" % (current_time ))


            """root = Tk()
            buttonw1 = ttk.Button(root, text = "Launch MRT Site")"""

            #
            label2 = tk.Label(root,text='Repairs').grid(row = 0, column = 2)
            b2 = tk.Button(root, text="Launch", command=create_window1)
            b2.grid(column = 3, row = 0)

            """root = Tk()
            buttonw1 = ttk.Button(root, text = "Launch MRT Site")"""


            #

            label3 = tk.Label(root,text='Services').grid(row = 0, column = 8)
            b3 = tk.Button(root, text="Launch", command=create_window2)
            b3.grid(column = 9, row = 0)

            label4 = tk.Label(root,text='Time Management').grid(row = 0, column = 10)
            b3 = tk.Button(root, text="Launch", command=create_window3)
            b3.grid(column = 11, row = 0)

            label5 = tk.Label(root,text='Items').grid(row = 0, column = 12)
            b3 = tk.Button(root, text="Launch", command=create_window4)
            b3.grid(column = 13, row = 0)

            label6 = tk.Label(root,text='Customer Requests').grid(row = 0, column = 14)
            b3 = tk.Button(root, text="Launch", command=create_window5)
            b3.grid(column = 15, row = 0)

            
            root.title("MRT | Home Page")
            root.geometry("980x750")

            #root1 = Tk()
            buttonsite = ttk.Button(root, text = "Launch MRT Site")
            buttonsite.grid(column = 18, row = 0,sticky=E)

            def mrtsite():
                webbrowser.open("http://www.mobilerepairtechs.com")
                print('Opened Web site using launch MRT Site')

            buttonsite.config(command = mrtsite)

            logo = PhotoImage(file = 'I:/Projects\Mobile Repair Techs/MRT Media/Mobile repair tech logo files/final_vector_logo.gif')
            #buttonsite.config(image= logo ,compound= 'center')


            """root = Tk()
            buttonw1 = ttk.Button(root, text = "Launch MRT Site")"""


                        
            #main program end?

        elif uncontent == "":
            message = "Enter a username..."
            
        elif content == "":
            message = "Enter a password..."
            

        else:
            message = "Acceess Denied..."

        self.text.delete(0.0,END)
        self.text.insert(0.0, message,)


app = Application(root)

root.mainloop()
