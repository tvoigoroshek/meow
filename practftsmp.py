from tkinter import *
tk = Tk()
tk.geometry('650x750')
tk.title("PracticeFutureSimpleTense")

lbl = Label(tk, text="Put the words in correct form:", font=("",16))
lbl.grid(column=0, row=0)
lbl.pack()

lbl1 = Label(tk, text="Joan thinks the Conservatives_____(win) the next election. ", font=("",12))
lbl1.pack()

lbl1change = Label(tk, text="", font=("",12))
lbl1change.pack()
def qwertt1():
    e=edit1.get()
    lbl1change.config(text=(e,"/will win"))
    
edit1=Entry(tk,width=20,bg='white')
edit1.pack()
##
##

lbl2 = Label(tk, text=" If she passes the exam, she ______(be) very happy. ", font=("",12))
lbl2.pack()

lbl2change = Label(tk, text="", font=("",12))
lbl2change.pack()
def qwertt2():
    e=edit2.get()
    lbl2change.config(text=(e,"/will be"))
edit2=Entry(tk,width=20,bg='white')
edit2.pack()    
    
##
##

lbl3 = Label(tk, text="I _____(be) there by four o'clock I promise ", font=("",12))
lbl3.pack()

lbl3change = Label(tk, text="", font=("",12))
lbl3change.pack()
def qwertt3():
    e=edit3.get()
    lbl3change.config(text=(e,"/will be"))
edit3=Entry(tk,width=20,bg='white')
edit3.pack()    
    

##
##

lbl4 = Label(tk, text="The meeting ____(take) place at 6pm", font=("",12))
lbl4.pack()

lbl4change = Label(tk, text="", font=("",12))
lbl4change.pack()
def qwertt4():
    e=edit4.get()
    lbl4change.config(text=(e,"/will take"))
edit4=Entry(tk,width=20,bg='white')
edit4.pack()    
    

##
##
lbl5 = Label(tk, text="If you eat all of that cake, you ____(feel) sick.", font=("",12))
lbl5.pack()

lbl5change = Label(tk, text="", font=("",12))
lbl5change.pack()
def qwertt5():
    e=edit5.get()
    lbl5change.config(text=(e,"/will feel"))
edit5=Entry(tk,width=20,bg='white')
edit5.pack()    

##
##
lbl6 = Label(tk, text="They ____(be) home at 10 o'clock.", font=("",12))
lbl6.pack()

lbl6change = Label(tk, text="", font=("",12))
lbl6change.pack()
def qwertt6():
    e=edit6.get()
    lbl6change.config(text=(e,"/will be"))
edit6=Entry(tk,width=20,bg='white')
edit6.pack()    
    

##
##
lbl7= Label(tk, text="We (eat) _______ pasta tomorrow", font=("",12))
lbl7.pack()

lbl7change = Label(tk, text="", font=("",12))
lbl7change.pack()
def qwertt7():
    e=edit7.get()
    lbl7change.config(text=(e,"/will eat"))
edit7=Entry(tk,width=20,bg='white')
edit7.pack()    


##
##

lbl8 = Label(tk, text="I'm afraid I ______(not/be) able to come tomorrow", font=("",12))
lbl8.pack()

lbl8change = Label(tk, text="", font=("",12))
lbl8change.pack()
def qwertt8():
    e=edit8.get()
    lbl8change.config(text=(e,"/won`t be"))
edit8=Entry(tk,width=20,bg='white')
edit8.pack()    


##
##

lbl9= Label(tk, text="Because of the train strike, the meeting _____(not/take) place at 9 o'clock..", font=("",12))
lbl9.pack()

lbl9change = Label(tk, text="", font=("",12))
lbl9change.pack()
def qwertt9():
    e=edit9.get()
    lbl9change.config(text=(e,"/won`t take"))
edit9=Entry(tk,width=20,bg='white')
edit9.pack()   
    
##
##
lbl10 = Label(tk, text=" If it rains, we _____(not/go) to the beach", font=("",12))
lbl10.pack()

lbl10change = Label(tk, text="", font=("",12))
lbl10change.pack()
def qwertt10():
    e=edit10.get()
    lbl10change.config(text=(e,"/won`t go"))
    
edit10=Entry(tk,width=20,bg='white')
edit10.pack()

btn=Button(tk,text="confirm",command=lambda:(qwertt1(),qwertt2(),qwertt3(),qwertt4(),qwertt5(),qwertt6(),qwertt7(),qwertt8(),qwertt9(),qwertt10()))
btn.pack()
tk.mainloop()



