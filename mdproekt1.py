from tkinter import *
from PIL import ImageTk, Image

meow="FutureSimpleRules.jpg"
meow1="PresentSimpleRules.jpg"
meow2="PastSimpleRules.jpg"
def rules():
    tk=Tk()
    tk.title("rules")
    lbl = Label(tk, text="Choose one of the topics:", font=("",16))
    lbl.grid(column=0, row=0)
    def clicked1():
        root = Tk()
        root.title("Past Simple")
        root.geometry('820x800')
        img = ImageTk.PhotoImage(Image.open(meow2))
        imglabel = Label(root, image=img).grid(row=1, column=1) 
        root.mainloop()
    def clicked2():
        root = Tk()
        root.title("Present Simple")
        root.geometry('820x800')
        img = ImageTk.PhotoImage(Image.open(meow1))
        imglabel = Label(root, image=img).grid(row=1, column=1) 
        root.mainloop()
    def clicked3():
        root = Tk()
        root.title("Future Simple")
        root.geometry('820x800')
        img = ImageTk.PhotoImage(Image.open(meow))
        imglabel = Label(root, image=img).grid(row=1, column=1) 
        root.mainloop()
    
    btn = Button(tk, text="Past Simple",command=clicked1)
    btn.grid(column=0, row=2)
    btn1 = Button(tk, text="Present Simple",command=clicked2)
    btn1.grid(column=0, row=3)
    btn2 = Button(tk, text="Future Simple",command=clicked3)
    btn2.grid(column=0, row=4)
    
    
    tk.mainloop()

    
rules()

        
