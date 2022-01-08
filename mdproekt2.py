from tkinter import *
def practice():
    tk = Tk()
    tk.title("practice")
    lbl = Label(tk, text="Choose one of the topics:", font=("",16))
    lbl.grid(column=0, row=0)
    def clicked1():
        import practpssmp
    def clicked2():
        import practprsmp
    def clicked3():
        import practftsmp
        
        
    btn = Button(tk, text="Past Simple",command=clicked1)
    btn.grid(column=0, row=2)
    btn1 = Button(tk, text="Present Simple",command=clicked2)
    btn1.grid(column=0, row=3)
    btn2 = Button(tk, text="Future Simple",command=clicked3)
    btn2.grid(column=0, row=4)
    
    tk.geometry('250x150')
    tk.mainloop()

    
practice()
