#Author guo
import  tkinter as tk
window=tk.Tk()
window.title('my window')
window.geometry('500x500')

l=tk.Label(window,text='',bg='yellow')
l.pack()
counter=0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1
menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='file',menu=filemenu)#加上项目
menubar.add_command(label='NEW',command=do_job)
menubar.add_command(label='open',command=do_job)
menubar.add_command(label='save',command=do_job)
menubar.add_separator()
menubar.add_command(label='setting',command=do_job)
menubar.add_command(label='exit',command=window.quit)
window.config(menu=menubar)
window.mainloop()