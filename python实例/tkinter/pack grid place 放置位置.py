#Author guo
import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('200x200')
'''
tk.Label(window,text=1).pack(side='top')
tk.Label(window,text=1).pack(side='bottom')
tk.Label(window,text=1).pack(side='right')
tk.Label(window,text=1).pack(side='left')
'''

# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i,column=j)

#最常用
tk.Label(window,text=1).place(x=10,y=100,anchor='nw')#把一角锚定
window.mainloop()