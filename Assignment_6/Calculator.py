from tkinter import *
window = Tk()
window.geometry("520x420")
window.title("CALCULATOR")
window.resizable(False, False)
window.config(bg="white")
math=0
e = Entry(window, width=56, borderwidth=5,justify=RIGHT)
def click(num):
    e.insert(END, str(num))
def clear():
    e.delete(0, END)
def add():
    n1 = e.get()
    global math
    math = "Addition"
    global i
    i = int(n1)
    e.delete(0, END)
def div():
    n1 = e.get()
    global math
    math = "Division"
    global i
    i = int(n1)
    e.delete(0, END)
def sub():
    n1 = e.get()
    global math
    math = "Subtraction"
    global i
    i = int(n1)
    e.delete(0, END)
def mul():
    n1 = e.get()
    global math
    math = "Multiplication"
    global i
    i = int(n1)
    e.delete(0, END)


b = Button(window,text="1", width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(1))
b.place(x=0, y=50)
b = Button(window,text="2",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(2))
b.place(x=130, y=50)
b = Button(window,text="3", width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(3))
b.place(x=260, y=50)
b = Button(window,text="4", width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(4))
b.place(x=0, y=130)
b = Button(window,text="5",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(5))
b.place(x=130, y=130)
b = Button(window,text="6", width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(6))
b.place(x=260, y=130)
b = Button(window,text="7", width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(7))
b.place(x=0, y=210)
b = Button(window,text="8",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(8))
b.place(x=130, y=210)
b = Button(window,text="9", width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(9))
b.place(x=260, y=210)
b = Button(window,text="0",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command= lambda:click(0))
b.place(x=0, y=290)
b = Button(window,text="+",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command=lambda:add())
b.place(x=390, y=50)

b = Button(window,text="-",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command=lambda:sub())
b.place(x=390, y=130)

b = Button(window,text="*",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black",command=lambda:mul())
b.place(x=390, y=210)
b = Button(window,text="/",width=10,height=2,fg="green",bg="black",activebackground="green",activeforeground="black",command=lambda:div())
b.place(x=390, y=290)
b = Button(window,text="CLEAR",width=53,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command=lambda:clear())
b.place(x=0, y=370)
def equal():
    n2=e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, i+ int(n2))
    elif math == "Subtraction":
        e.insert(0,i-int(n2))
    elif math=="Multiplication":
        e.insert(0,i*int(n2))
    elif math=="Division":
        e.insert(0, i/int(n2))
b = Button(window,text="=",width=24,height=2,fg="green",bg="black",activebackground="green",activeforeground="black", command=lambda:equal())
b.place(x=130, y=290)
e.place(x=0,y=0)
mainloop()