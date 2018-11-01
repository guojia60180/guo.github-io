#Author guo
import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('500x500')
#listbox 许多选项可供选择 传参数 至print
var1=tk.StringVar()
var2=tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()
e=tk.Entry(window,show='*')
e.pack()
var2.set((11,22,33,44,55))
lb=tk.Listbox(window,listvariable=var2)
list_items=[1,2,3,4,5]
for item in list_items:
    lb.insert('end',item)
# lb.insert(1,'first')
# lb.insert(2,'second')
# lb.delete(2)
lb.pack()
def insert_point():
    var=e.get()
    lb.insert(1,var)
def insert_end():
    var=e.get()
    lb.insert(2,var)
def print_selection():
    value=lb.get(lb.curselection())#光标选择的东西
    var1.set(value)
b=tk.Button(window,text='print selection',width=15,
            height=2,command=print_selection)
b.pack()

b2=tk.Button(window,text='insert1 ',width=15,height=2,command=insert_point())
b2.pack()
b3=tk.Button(window,text='insert2 ',width=15,height=2,command=insert_end())
b3.pack()


# var2.set((11,22,33,44,55))
# lb=tk.Listbox(window,listvariable=var2)
# list_items=[1,2,3,4,5]
# for item in list_items:
#     lb.insert('end',item)
# lb.insert(1,'first')
# lb.insert(2,'second')
# lb.delete(2)
# lb.pack()

window.mainloop()