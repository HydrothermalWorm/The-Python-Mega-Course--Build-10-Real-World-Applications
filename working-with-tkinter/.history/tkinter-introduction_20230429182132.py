from tkinter import *

window = Tk()

b1=Button(window,text="Execute")
b1.grid(row=0,column=0)

e1=Entry(window,height=2,text="Put Your Text Here")
e1.grid(row=0,column=1)

t1=Text(window,height=2,width=20)
t1.grid(row=0,column=2)




window.mainloop()