#Author guo
import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('500x500')

canvas=tk.Canvas(window,
                 bg='white',
                 height=100,
                 width=200)
#image_file=tk.PhotoImage(file='.jpg') 用来加载文件
#image=canvas.create_image(0,0,anchor='nw',image=image_file)
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')#yuan
arc=canvas.create_arc(x0,y0,x1,y1,start=0,extent=180)#shan
rect=canvas.create_rectangle(x0,y0,x1,y1)
canvas.pack()
def moveit():
    canvas.move(rect,1,0)
b=tk.Button(window,text='move',command=moveit).pack()
window.mainloop()