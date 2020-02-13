from tkinter import *

def update_add():
    update("add")

def update_subtract():
    update("subtract")

def update_reset():
    update("reset")

window = Tk()
total=0
sum = Label(window)
sum.grid(row=0, column=1, columnspan=2)
label = Label(window, text="현재 합계:")
label.grid(row=0, column=0)
entry = Entry(window)
entry.grid(Row=1,column=0,columnspan=3)

add_button = Button(window,text="더하기(+)",command=update_add)
subtract_button = Button(window,text="빼기(-)",command=update_subtract)
reset_button = Button(window,text="초기화",command=update_reset)

add_button.grid(row=2,column=0)
subtract_button.grid(row=2,column=1)
reset_button.grid(row=2,column=2)

def update(method):
    global total
    if method == "add":
        total+=int(entry.get())
    if method == "subtract":
        total-=int(entry.get())
    if method == "reset":
        total=0
    sum["text"]=str(total)
    entry.delete(0,END)

window.mainloop()