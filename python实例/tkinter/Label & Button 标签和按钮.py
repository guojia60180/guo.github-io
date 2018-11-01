#Author guo
import tkinter as tk

window=tk.Tk()#建立一个窗口
window.title('mywindow')#mingzi
window.geometry('200x100')#设置长宽
var=tk.StringVar()#字符串变量
l=tk.Label(window,textvariable=var,bg='yellow',font=('Arial',12),width=15,height=2)
#在window上创建一个label

l.pack()#放置左右

on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit==True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
b=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
b.pack()
window.mainloop()#会刷新window