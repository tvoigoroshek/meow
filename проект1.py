from tkinter import *

def start():
    tk = Tk()
    tk.title("App")

    lbl = Label(tk, text="App for learning english!Choose practice or rules to start learning: ", font=("",16))
    lbl.grid(column=0, row=0)
    def clicked():
        import mdproekt1
    def clicked1():
        import mdproekt2
        
    btn = Button(tk, text="rules", command=clicked)
    btn.grid(column=0, row=2)
    btn = Button(tk, text="practice", command=clicked1)
    btn.grid(column=0, row=3)

    tk.geometry('620x100')
    tk.mainloop()


start()
