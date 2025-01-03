from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
top=Tk()
top.title('Login Form')
top.geometry('600x400')
top.config(bg='white')
top.resizable(False,False)
logo=ImageTk.PhotoImage(Image.open('images/logo.png'))
def login():
    if user_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror('Login','Enter Username and Password')
    elif user_entry.get()=='admin' and password_entry.get()=='admin':
        messagebox.showinfo('Login','Connected')
        top.update()
        top.destroy()
        import StudentManagement
    else:
         messagebox.showinfo('Login','Not Connected')
def show_hide_password():
    if password_entry['show']=='*':
        password_entry.config(show='')
        password_symbol.config(text='🔓',fg='orange',bg='white',bd=0,font=('Times',25))
    else:
        password_entry.config(show='*')
        password_symbol.config(text='🔒',fg='orange',bg='white',bd=0,font=('Times',25))
title_label=Label(top,text='Login Form',font=('Arial',40,'bold'),bg='white',fg='orangered').place(x=160,y=0)
title_logo=Button(top,image=logo,bd=0)
title_logo.place(x=240,y=70)
user_label=Label(top,text='Username',font=('Times',25),fg='blue',bg='white')
user_label.place(x=60,y=175)
password_label=Label(top,text='Password',font=('Times',25),fg='blue',bg='white')
password_label.place(x=60,y=245)
user_entry=Entry(top,width=18,font=('Times',20),fg='black',bg='white')
user_entry.place(x=240,y=183)
user_symbol=Button(top,text='🤵',fg='orange',bg='white',bd=0,font=('Times',25))
user_symbol.place(x=510,y=170)
password_entry=Entry(top,width=18,font=('Times',20),fg='black',bg='white',show='*')
password_entry.place(x=240,y=248)
password_symbol=Button(top,text='🔒',fg='orange',bg='white',bd=0,font=('Times',25),command=show_hide_password)
password_symbol.place(x=510,y=235)
login_btn=Button(top,width=15,font=('Times',20),text='Login',bg='blue',fg='white',command=login)
login_btn.place(x=180,y=330)
top.mainloop()