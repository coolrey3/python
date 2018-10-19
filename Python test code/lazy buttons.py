#demonstrates how to use a class with tkinter

from tkinter import *

class Application(Frame):
    """A GUI Application with three buttons"""
    def __init__(self,master):
        """Initialize the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks = 0 #count number of button clicks
        self.create_widgets()

    def create_widgets(self):
        """create 4 buttons taht do nothing """
        #create first button
        self.button1 = Button(self,text = "This is the first button")
        self.button1.grid()

        #create second button
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "This will show up text")

        #create third button
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "This will alsho show text"


        #creates the total clicks event listener button
        self.button = Button(self)
        self.button["text"] = "Total Clicks:"
        self.button["command"]= self.update_count
        self.button.grid()

    def update_count(self):
        """increase the click count and display the new total"""
        self.button_clicks += 1
        self.button["text"] = "Total Clicks: " + str(self.button_clicks)


root = Tk()
root.title("Lazy buttons bish")
root.geometry("230x120")

app = Application(root)
