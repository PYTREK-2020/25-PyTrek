from tkinter import *
import automation as at


root = Tk()


def fun():
    # at.speak('heloo')
    # while True:
    #
    #     at.recogniser()
    lb1 = Label(root, text='Entre the location of the software you want to open')
    lb1.grid(row=1, column=0)

    but = Button(root, text='gg', command=cli)
    but.grid(row=2, column=1)

e1 = Entry(root)
e1.grid(row=2, column=0)

def cli():
    global a1
    a1 = e1.get()
    lab=Label(root, text=a1)
    lab.grid(row=3, column=0)
    print(a1)


btn1 = Button(root, text='hello', command=fun,padx=50, pady=40)
btn2 = Button(root, text='2', command=fun, padx=50, pady=40)
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)

root.mainloop()

