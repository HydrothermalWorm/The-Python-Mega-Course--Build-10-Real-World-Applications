from tkinter import *

window=Tk()

# Title entry
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

# Author entry
l2=Label(window,text="Author")
l2.grid(row=1,column=0)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=1,column=1)

# Year entry
l3=Label(window,text="Year")
l3.grid(row=0,column=2)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)






isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)


window.mainloop()
