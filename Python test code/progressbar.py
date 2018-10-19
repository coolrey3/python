from tkinter import *
from tkinter import ttk
root = Tk()
progressbar = ttk.Progressbar(root, orient = HORIZONTAL , length = 200)
progressbar.pack()
progressbar.config (mode = 'indeterminate')
progressbar.start()
#progressbar.stop()
progressbar.config(mode = 'determinate' ,maximum = 11.0,value = 4.2)
prgressbar.config(value = 4.0)

