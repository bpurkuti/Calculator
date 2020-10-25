
from tkinter import*

root = Tk()

def addBtn():
    myLabel = Label(root, text="Click! Click!")
    myLabel.grid(row=5,column=5)
a=b=c=0
btnlist = []
for i in range (1,10):
    if(i<4):
        myBtn = Button(root, text=i, command=addBtn).grid(row=0, column=a)
        btnlist.append(myBtn)
        a+=1
    elif(i<7):
        myBtn = Button(root, text=i).grid(row=1, column=b)
        btnlist.append(myBtn)
        b+=1
    else:
        myBtn = Button(root, text=i).grid(row=2, column=c)
        btnlist.append(myBtn)
        c+=1

#btnlist[1].grid(row=5, column=5)

root.mainloop()


