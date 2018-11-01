#Author guo
#目的是做一个登录窗口

import tkinter as tk
from tkinter import messagebox
import pickle
window=tk.Tk()
window.title('for logging')
window.geometry('500x500')
#图片的放置
canvas=tk.Canvas(window,height=200,width=500)
image_file=tk.PhotoImage(file='1.jpg')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')
#输入文本框，密码以密文表示
tk.Label(window,text='User name:').place(x=50,y=170)
tk.Label(window,text='Password:').place(x=50,y=210)
var_usr_name=tk.StringVar()
var_usr_name.set('guojia60180@gmail.com')
entryname=tk.Entry(window,textvariable=var_usr_name)
entryname.place(x=160,y=170)
var_usr_pwd=tk.StringVar()
entrypwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entrypwd.place(x=160,y=210)
#用户处理信息函数
def usr_login():
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usr_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usr_info={'admin':'admin'}
            pickle.dump(usr_info,usr_file)
    if usr_name in usr_info:
        if usr_pwd == usr_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        ##如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果发现用户名不存在
        is_sign_up = tk.messagebox.askyesno('Welcome',
                                            'You have not sign up yet. Sign up today?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_signup()
def usr_signup():
    def sign_to_new():
        ##以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        ##这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)

        ##这里就是判断，如果两次密码输入不一致，则提示`'Error', 'Password and confirm password must be the same!'`
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')

        ##如果用户名已经在我们的数据文件中，则提示`'Error', 'The user has already signed up!'`
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')

        ##最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功`'Welcome', 'You have successfully signed up!'`
        ##然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            ##然后销毁窗口。
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')
    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set('example@python.com')  # 将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=150, y=10)  # `entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    # 下面的 sign_to_Mofan_Python 我们再后面接着说
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_new)
    btn_comfirm_sign_up.place(x=150, y=130)
#登录按钮
btn_login=tk.Button(window,text='Login',command=usr_login)
btn_login.place(x=170,y=230)
btn_signup=tk.Button(window,text='sign up',command=usr_signup)
btn_signup.place(x=270,y=230)
window.mainloop()