from tkinter import*
import os

root = Tk()

root.title("Basic Calculator")
e = Entry(root,width=60,borderwidth=10, fg="white", bg="green")
e.grid(row= 0, column=0, columnspan=5, padx=10, pady=10)

current=0
token=""

def btn_click(num):
   curr = e.get()
   e.delete(0,END)
   e.insert(0,str(curr)+str(num))
   return

def funcBtn(func):
   global token
   global current
   current = e.get()
   if(func=='+'):
      token = "add"
   if(func=='-'):
      token = "sub"
   if(func=='÷'):
      token = "div"
   if(func=='×'):
      token = "mult" 
   clrBtn()

   return

def eqlBtn():
   global token
   global current

   if(token=="add"):
      result = float(current)+float(e.get())
   elif(token=="sub"):
      result = float(current)-float(e.get())
   elif(token=="div"):
      result = float(current)/float(e.get())
   elif(token=="mult"):
      result = float(current)*float(e.get())
   else:
      return
   e.delete(0,END)
   e.insert(0,result)

   token=""
   current=0
   return


def clrBtn():
   e.delete(0,END)
   current=0
   token=""
   return



#Numerical Buttons
btn_1 = Button(root, text= "1",padx = 40, pady=20, command = lambda: btn_click(1))
btn_2 = Button(root, text= "2",padx = 40, pady=20, command = lambda: btn_click(2) )
btn_3 = Button(root, text= "3",padx = 40, pady=20, command = lambda: btn_click(3) )
btn_4 = Button(root, text= "4",padx = 40, pady=20, command = lambda: btn_click(4) )
btn_5 = Button(root, text= "5",padx = 40, pady=20, command = lambda: btn_click(5) )
btn_6 = Button(root, text= "6",padx = 40, pady=20, command = lambda: btn_click(6) )
btn_7 = Button(root, text= "7",padx = 40, pady=20, command = lambda: btn_click(7) )
btn_8 = Button(root, text= "8",padx = 40, pady=20, command = lambda: btn_click(8) )
btn_9 = Button(root, text= "9",padx = 40, pady=20, command = lambda: btn_click(9) )
btn_0 = Button(root, text= "0",padx = 40, pady=20, command = lambda: btn_click(0) )

btn_1.grid(row= 3, column=0)
btn_2.grid(row= 3, column=1)
btn_3.grid(row= 3, column=2)

btn_4.grid(row= 2, column=0)
btn_5.grid(row= 2, column=1)
btn_6.grid(row= 2, column=2)

btn_7.grid(row= 1, column=0)
btn_8.grid(row= 1, column=1)
btn_9.grid(row= 1, column=2)

btn_0.grid(row= 4, column=1)


#Function buttons
btn_add = Button(root, text= "+",padx = 40, pady=20, command = lambda: funcBtn("+") )
btn_sub = Button(root, text= "-",padx = 40, pady=20, command = lambda: funcBtn("-") )
btn_mult = Button(root, text= "×",padx = 40, pady=20, command = lambda: funcBtn("×") )
btn_div = Button(root, text= "÷",padx = 40, pady=20, command = lambda: funcBtn("÷") )
btn_clr = Button(root, text= "C",padx = 40, pady=20, command = clrBtn )
btn_eql = Button(root, text= "=",padx = 40, pady=20, command = eqlBtn )


btn_add.grid(row= 2, column=3)
btn_sub.grid(row= 3, column=3)
btn_mult.grid(row= 4, column=2)
btn_div.grid(row= 4, column=0)
btn_clr.grid(row= 1, column=3)
btn_eql.grid(row= 4, column=3)


root.mainloop()


