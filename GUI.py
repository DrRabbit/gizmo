from Tkinter import *


def f():
    print('hello')

def g():
    pass


root = Tk()
root.geometry('400x400')


width = root.winfo_width()
height = root.winfo_height()
print(width, height)

root.title("Gizmo")
# root.configure(bg='default')

button = Button(root,
                text="",
                fg="green",
                bg="black",
                highlightcolor='black',
                activeforeground='green',
                # font=('Calibri', 8, 'normal'),
                relief='raised',
                command=f,
                height=1,
                width=5,
                activebackground='black')

button.place(x=50, y=50)
'''
btn2 = Button(root,
              text="Button 2",
              fg="green",
              bg="black",
              highlightcolor='black',
              activeforeground='green',
              font=('Calibri', 14, 'normal'),
              relief='raised',
              activebackground='black')

btn2.place(x=200, y=50)


lbl = Label(root, text='Date')
lbl.place(x=100, y=100)
label_1 = Label(root, text='Date')
label_1.grid(row=0, column=0)

e = Entry(root)
# e.insert(END, 'hello')

# e.grid(row=0, column=1, sticky='NSEW')
# e = Entry(root)
e.grid(row=0, column=0, sticky='NSEW')
'''


# root.resizable(width=False, height=False)
root.mainloop()



