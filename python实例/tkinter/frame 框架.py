#Author guo
import tkinter as tk

window=tk.Tk()
window.title('1')
window.geometry('500x500')
tk.Label(window,text='on thenwindow').pack()

frm=tk.Frame(window)
frm.pack()
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l,text='on the frm1').pack()
tk.Label(frm_r,text='on the frm2').pack()

window.mainloop()