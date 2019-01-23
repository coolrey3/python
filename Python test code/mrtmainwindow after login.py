from tkinter import *
from tkinter import ttk
import webbrowser

root = Tk()
logo = PhotoImage(file = 'C:\github\Frontend\Images\BG\OOF-desk.png')


#Hero Rule
def Nazeebo():
    webbrowser.open("http://www.heroesfire.com/hots/guide/nazebo-the-build-2346")
    print('clicked')

#Nazeebo Button
buttonsite = ttk.Button(root, text = "Nazeebo Build")
buttonsite.grid(column = 1,row = 0)
buttonsite.config(command = Nazeebo)
buttonsite.config(image=logo,compound= 'left')


#Jaina Rule
def Jaina():
    webbrowser.open("http://www.heroesfire.com/hots/wiki/heroes/jaina")
    print('clicked')

#Jaina Button
buttonsite = ttk.Button(root, text = "Jaina Build  ")
buttonsite.grid(column = 2,row = 0)
buttonsite.config(command = Jaina)
buttonsite.config(image=logo,compound= 'left')
    
#illidan Rule  
def illidan():
    webbrowser.open("http://www.heroesfire.com/hots/wiki/heroes/illidan")
    print('clicked')
    
#illidan Button
buttonsite = ttk.Button(root, text = "illidan Build")
buttonsite.grid(column = 3,row = 0)
buttonsite.config(command = illidan)
buttonsite.config(image=logo,compound= 'left')
    
#Kael'thas Rule
def kaelthas():
    webbrowser.open("http://www.heroesfire.com/hots/wiki/heroes/kaelthas")
    print('clicked')

#Kael'thas Button
buttonsite = ttk.Button(root, text = "Kael'thas Build")
buttonsite.grid(column = 1,row = 1)
buttonsite.config(command = kaelthas)
buttonsite.config(image=logo,compound= 'left')

#Hero Rule
def etc():
    webbrowser.open("http://www.heroesfire.com/hots/wiki/heroes/elite-tauren-chieftain")
    print('clicked')

#Hero Button
buttonsite = ttk.Button(root, text = "etc Build")
buttonsite.grid(column = 2,row = 1)
buttonsite.config(command = etc)
buttonsite.config(image=logo,compound= 'left')

#Hero Rule
def Zeratul():
    webbrowser.open("http://www.heroesfire.com/hots/wiki/heroes/zeratul")
    print('clicked')

#Hero Button
buttonsite = ttk.Button(root, text = "Zeratul Build")
buttonsite.grid(column = 3,row = 1)
buttonsite.config(command = Zeratul)
buttonsite.config(image=logo,compound= 'left')





small_logo = logo.subsample(5,5)
#button.config(image=small_logo)
#label.img = logo
#label.config(image=label.img)







root.title('MRT Device Manager')
root.mainloop()
