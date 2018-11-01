#Author guo
import tkinter as tk
#scale 返回一个数字
window=tk.Tk()
window.title('my window')
window.geometry('500x500')

l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection(v):
    l.config(text='you select'+v)

s=tk.Scale(window,label='try me',from_=5,to=10,
           orient=tk.HORIZONTAL,
           length=200,
           showvalue=False,
           tickinterval=1,
           resolution=0.01,
           command=print_selection)
s.pack()

window.mainloop()