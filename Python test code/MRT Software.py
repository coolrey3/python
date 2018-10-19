#import module
import tkinter

#set frame
root = tkinter.Tk()
root.title("Mobile Repair Techs Device Manager")
root.geometry("400x400")
app = tkinter.Frame(root)
app.grid()

#adds labels
label = tkinter.Label(app, text = "Time Management System")
label.grid()

#adds buttons
button1 = tkinter.Button(app, text = "Clock In")
button1.grid()

button2= tkinter.Button(app)
button2.grid()
button2.configure(text = "this will show text")

button3= tkinter.Button(app)
button3.grid()
button3["text"] = "This will show up as well."

#kicks off the even loop
root.mainloop()
