from tkinter import*
import os

root = Tk()

e = Entry(root,width=50,borderwidth=10, fg="white", bg="green")
e.pack()
e.insert(0,"Enter Something here")

def addBtn():
   hello = "Hello " + e.get()
   myLabel = Label(root, text=hello)
   myLabel.pack()




myBtn = Button(root, text="Hello", command=addBtn)
myBtn.pack()

root.mainloop()


