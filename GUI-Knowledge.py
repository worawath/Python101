from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #main Program
GUI.title('โปรแกรมบันทึกข้อมูล') #name of Program
GUI.geometry('500x400') #size of Program

B1 = ttk.Button(GUI,text='แสดงจำนวนเงิน')
B1.pack(ipadx=20,ipady=20)

#########################
def Button2():
      text = 'จำนวนเงินในบัญชีมี 999 บาท'
      messagebox.showinfo('จำนวนเงิน',text)

FB1 = Frame(GUI)
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='แสดงจำนวนเงิน', command=Button2)
B2.pack(ipadx=20,ipady=20)
#########################


GUI.mainloop()

