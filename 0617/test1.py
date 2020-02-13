from tkinter import *

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0,str(mytemp))


window = Tk()

l1 = Label(window, text="화씨", font='helvetica 16 italic')
l2 = Label(window, text="화씨", font='helvetica 16 italic')
l1.grid(row=0, column=0)
l1.grid(row=1, column=0)

e1 = Entry(window, bg="yellow", fg="white")
e2 = Entry(window, bg="yellow", fg="white")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=process)
b2 = Button(window, text="섭씨->화씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

window.mainloop()