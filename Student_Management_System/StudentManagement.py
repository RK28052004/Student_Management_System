from tkinter import*
import tkinter as tk
from tkinter import ttk
import time
import mysql.connector
from tkinter import messagebox,filedialog
import pandas
top=Tk()
top.geometry('1400x1400')
top.config(bg='white')
top.title('Student Management System')
count=0
text=''
def database_connection():
    root=Tk()
    root.geometry('650x400')
    root.config(bg='white')
    root.title('Database Connection')
    root.resizable(False,False)
    def connect_database():
        global mycursor,mydb
        try:
            mydb=mysql.connector.connect(
                host=host_entry.get(),
                user=user_entry.get(),
                password=password_entry.get()
            )
            mycursor=mydb.cursor()
        except:
            messagebox.showerror('Error','Connection Error',parent=root)
            return
        try:
            sql='create database student'
            mycursor.execute(sql)
            sql='use student'
            mycursor.execute(sql)
            sql='create table details(Id int primary key,Name varchar(40),Mobile_No varchar(40),Email varchar(40),Address varchar(40),Gender varchar(40),Dob varchar(40),Added_Date varchar(40),Added_Time varchar(40))'
            mycursor.execute(sql)
        except:
            sql='use student'
            mycursor.execute(sql)
        messagebox.showinfo('Connection','Database Connected Successfully',parent=root)
        root.destroy()
        add_btn.config(state=NORMAL,command=add_student)
        search_btn.config(state=NORMAL,command=search_student)
        delete_btn.config(state=NORMAL,command=delete_student)
        update_btn.config(state=NORMAL,command=update_student)
        show_btn.config(state=NORMAL,command=show_student)
        export_btn.config(state=NORMAL,command=export_data)
        exit_btn.config(state=NORMAL,command=exit)
    title_label=Label(root,text='Database Connection',font=('Arial',30,'italic bold'),bg='white',fg='orangered')
    title_label.place(x=125,y=0)
    host_label=Label(root,text='Host Name',font=('Times',25),fg='orange',bg='white')
    host_label.place(x=100,y=110)
    user_label=Label(root,text='User Name',font=('Times',25),fg='orange',bg='white')
    user_label.place(x=100,y=180)
    password_label=Label(root,text='Passsword',font=('Times',25),fg='orange',bg='white')
    password_label.place(x=100,y=250)
    host_entry=Entry(root,width=18,font=('Times',20),fg='black',bg='white')
    host_entry.place(x=300,y=115)
    user_entry=Entry(root,width=18,font=('Times',20),fg='black',bg='white')
    user_entry.place(x=300,y=185)
    password_entry=Entry(root,width=18,font=('Times',20),fg='black',bg='white',show='*')
    password_entry.place(x=300,y=255)
    connect_btn=Button(root,width=15,font=('Times',20),text='Login',bg='blue',fg='white',command=connect_database)
    connect_btn.place(x=210,y=320)
def add_student():
    add=Toplevel()
    add.geometry('650x650')
    add.config(bg='white')
    add.title('Add Student')
    add.resizable(False,False)
    add.grab_set()
    def add_data():
        try:
            if id_entry.get()=='' or name_entry.get()=='' or mobile_entry.get()=='' or email_entry.get()=='' or address_entry.get()=='' or gender_entry.get()=='' or dob_entry.get()=='':
                messagebox.showerror('Error','All details are required',parent=add)
            else:
                sql='insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                val=(id_entry.get(),name_entry.get(),mobile_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),currentdate,currenttime)
                mycursor.execute(sql,val)
                mydb.commit()
                result=messagebox.askyesno('Confirm','Do you wan to clear the form?',parent=add)
                if result:
                    id_entry.delete(0,END)
                    name_entry.delete(0,END)
                    mobile_entry.delete(0,END)
                    email_entry.delete(0,END)
                    address_entry.delete(0,END)
                    gender_entry.delete(0,END)
                    dob_entry.delete(0,END)
                else:
                    pass
        except:
            messagebox.showerror('Error','Id cannot be repeated!',parent=add)
            return
        sql='select * from details'
        mycursor.execute(sql)
        fetched_data=mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            datalist=list(data)
            student_table.insert('',END,values=datalist)
    title_label=Label(add,text='Add Student',font=('Arial',30,'italic bold'),bg='white',fg='orangered')
    title_label.place(x=205,y=0)
    id_label=Label(add,text='Id',font=('Times',25),fg='orange',bg='white')
    id_label.place(x=100,y=110)
    name_label=Label(add,text='Name',font=('Times',25),fg='orange',bg='white')
    name_label.place(x=100,y=180)
    mobile_label=Label(add,text='Mobile_No',font=('Times',25),fg='orange',bg='white')
    mobile_label.place(x=100,y=250)
    email_label=Label(add,text='Email',font=('Times',25),fg='orange',bg='white')
    email_label.place(x=100,y=320)
    address_label=Label(add,text='Address',font=('Times',25),fg='orange',bg='white')
    address_label.place(x=100,y=390)
    gender_label=Label(add,text='Gender',font=('Times',25),fg='orange',bg='white')
    gender_label.place(x=100,y=460)
    dob_label=Label(add,text='Dob',font=('Times',25),fg='orange',bg='white')
    dob_label.place(x=100,y=530)
    id_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    id_entry.place(x=300,y=115)
    name_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    name_entry.place(x=300,y=185)
    mobile_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    mobile_entry.place(x=300,y=255)
    email_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    email_entry.place(x=300,y=325)
    address_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    address_entry.place(x=300,y=395)
    gender_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    gender_entry.place(x=300,y=465)
    dob_entry=Entry(add,width=18,font=('Times',20),fg='black',bg='white')
    dob_entry.place(x=300,y=535)
    add_student_btn=Button(add,width=15,font=('Times',15),text='Add Student',bg='blue',fg='white',command=add_data)
    add_student_btn.place(x=210,y=600)
def search_student():
    search=Toplevel()
    search.geometry('650x650')
    search.config(bg='white')
    search.title('Search Student')
    search.resizable(False,False)
    search.grab_set()
    def search_data():
        sql="select * from details where id=%s || name=%s || mobile_no=%s || email=%s || address=%s || gender=%s || dob=%s"
        val=(id_entry.get(),name_entry.get(),mobile_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get())
        mycursor.execute(sql,val)
        student_table.delete(*student_table.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            datalist=list(data)
            student_table.insert('',END,values=datalist)
    title_label=Label(search,text='Search Student',font=('Arial',30,'italic bold'),bg='white',fg='orangered')
    title_label.place(x=205,y=0)
    id_label=Label(search,text='Id',font=('Times',25),fg='orange',bg='white')
    id_label.place(x=100,y=110)
    name_label=Label(search,text='Name',font=('Times',25),fg='orange',bg='white')
    name_label.place(x=100,y=180)
    mobile_label=Label(search,text='Mobile_No',font=('Times',25),fg='orange',bg='white')
    mobile_label.place(x=100,y=250)
    email_label=Label(search,text='Email',font=('Times',25),fg='orange',bg='white')
    email_label.place(x=100,y=320)
    searchress_label=Label(search,text='Address',font=('Times',25),fg='orange',bg='white')
    searchress_label.place(x=100,y=390)
    gender_label=Label(search,text='Gender',font=('Times',25),fg='orange',bg='white')
    gender_label.place(x=100,y=460)
    dob_label=Label(search,text='Dob',font=('Times',25),fg='orange',bg='white')
    dob_label.place(x=100,y=530)
    id_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    id_entry.place(x=300,y=115)
    name_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    name_entry.place(x=300,y=185)
    mobile_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    mobile_entry.place(x=300,y=255)
    email_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    email_entry.place(x=300,y=325)
    address_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    address_entry.place(x=300,y=395)
    gender_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    gender_entry.place(x=300,y=465)
    dob_entry=Entry(search,width=18,font=('Times',20),fg='black',bg='white')
    dob_entry.place(x=300,y=535)
    search_student_btn=Button(search,width=15,font=('Times',15),text='Search Student',bg='blue',fg='white',command=search_data)
    search_student_btn.place(x=210,y=600)
def delete_student():
    indexing=student_table.focus()
    print(indexing)
    content=student_table.item(indexing)
    content_id=content['values'][0]
    sql="delete from details where id='%s'"
    mycursor.execute(sql,(content_id,))
    mydb.commit()
    messagebox.showinfo('Deleted', 'Details deleted successfully')
    sql='select * from details'
    mycursor.execute(sql)
    fetched_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        datalist=list(data)
        student_table.insert('',END,values=datalist)
def update_student():
    update=Toplevel()
    update.geometry('650x650')
    update.config(bg='white')
    update.title('Update Student')
    update.resizable(False,False)
    def update_data():
        sql='update details set name=%s,mobile_no=%s,email=%s,address=%s,gender=%s,dob=%s,added_date=%s,added_time=%s where id=%s'
        val=(name_entry.get(),mobile_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),currentdate,currenttime,id_entry.get())
        mycursor.execute(sql,val)        
        mydb.commit()
        messagebox.showinfo('Updated','Details updated successfully',parent=update)
        update.destroy()
        show_student()
    title_label=Label(update,text='Update Student',font=('Arial',30,'italic bold'),bg='white',fg='orangered')
    title_label.place(x=205,y=0)
    id_label=Label(update,text='Id',font=('Times',25),fg='orange',bg='white')
    id_label.place(x=100,y=110)
    name_label=Label(update,text='Name',font=('Times',25),fg='orange',bg='white')
    name_label.place(x=100,y=180)
    mobile_label=Label(update,text='Mobile_No',font=('Times',25),fg='orange',bg='white')
    mobile_label.place(x=100,y=250)
    email_label=Label(update,text='Email',font=('Times',25),fg='orange',bg='white')
    email_label.place(x=100,y=320)
    address_label=Label(update,text='Address',font=('Times',25),fg='orange',bg='white')
    address_label.place(x=100,y=390)
    gender_label=Label(update,text='Gender',font=('Times',25),fg='orange',bg='white')
    gender_label.place(x=100,y=460)
    dob_label=Label(update,text='Dob',font=('Times',25),fg='orange',bg='white')
    dob_label.place(x=100,y=530)
    id_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    id_entry.place(x=300,y=115)
    name_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    name_entry.place(x=300,y=185)
    mobile_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    mobile_entry.place(x=300,y=255)
    email_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    email_entry.place(x=300,y=325)
    address_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    address_entry.place(x=300,y=395)
    gender_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    gender_entry.place(x=300,y=465)
    dob_entry=Entry(update,width=18,font=('Times',20),fg='black',bg='white')
    dob_entry.place(x=300,y=535)
    update_student_btn=Button(update,width=15,font=('Times',15),text='Update Student',bg='blue',fg='white',command=update_data)
    update_student_btn.place(x=210,y=600)
    indexing=student_table.focus()
    content=student_table.item(indexing)
    listdata=content['values']
    id_entry.insert(0,listdata[0])
    name_entry.insert(0,listdata[1])
    mobile_entry.insert(0,listdata[2])
    email_entry.insert(0,listdata[3])
    address_entry.insert(0,listdata[4])
    gender_entry.insert(0,listdata[5])
    dob_entry.insert(0,listdata[6])
def show_student():
    sql='select * from details'
    mycursor.execute(sql)
    fetched_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        datalist=list(data)
        student_table.insert('',END,values=datalist)
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=student_table.get_children()
    newlist=[]
    for index in indexing:
        content=student_table.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile_No','Email','Address','Gender','Dob','Added_Date','Added_Time'])
    table.to_csv(url,index=False) 
    messagebox.showinfo('Details','Details inserted in excel successfully')
def exit():
    result=messagebox.askyesno('Confirm','Do you want to close the window?')
    if result:
        top.destroy()
    else:
        pass
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    title_label.config(text=text)
    count+=1
    title_label.after(300,slider)
def date_time():
    global currentdate,currenttime
    currentdate=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    date_time_label.config(text=f'Date : {currentdate}\nTime : {currenttime}')
    date_time_label.after(1000,date_time)
s='STUDENT MANAGEMENT SYSTEM'
title_label=Label(top,text=s,font=('Arial',30,'italic bold'),bg='white',fg='orangered',width=30)
title_label.place(x=315,y=0)
slider()
date_time_label=Label(top,font=('Times',20),bg='white',fg='orange')
date_time_label.place(x=10,y=10)
date_time()
database_btn=Button(top,text='Connect to Database',font=('Times',15),fg='black',bd=0,command=database_connection)
database_btn.place(x=1080,y=15)
right_frame=tk.Frame(top,bg='white')
right_frame.place(x=10,y=100,width=250,height=530)
add_btn=Button(top,text='Add Student',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
add_btn.place(x=45,y=130)
search_btn=Button(top,text='Search Student',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
search_btn.place(x=45,y=200)
delete_btn=Button(top,text='Delete Student',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
delete_btn.place(x=45,y=270)
update_btn=Button(top,text='Update Student',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
update_btn.place(x=45,y=340)
show_btn=Button(top,text='Show Student',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
show_btn.place(x=45,y=410)
export_btn=Button(top,text='Export Data',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
export_btn.place(x=45,y=480)
exit_btn=Button(top,text='Exit',font=('Times',15),fg='black',bd=0,state=DISABLED,command=add_student)
exit_btn.place(x=45,y=550)
left_frame=tk.Frame(top,bg='white')
left_frame.place(x=250,y=100,width=1000,height=530)
ScrollbarX=Scrollbar(left_frame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(left_frame,orient=VERTICAL)
student_table=ttk.Treeview(left_frame,columns=('Id','Name','Mobile_No','Email','Address','Gender','Dob','Added_Date','Added_Time'))
student_table.heading('Id',text='Id')
student_table.heading('Name',text='Name')
student_table.heading('Mobile_No',text='Mobile_No')
student_table.heading('Email',text='Email')
student_table.heading('Address',text='Address')
student_table.heading('Gender',text='Gender')
student_table.heading('Dob',text='Dob')
student_table.heading('Added_Date',text='Added_Date')
student_table.heading('Added_Time',text='Added_Time')
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)
ScrollbarX.config(command=student_table.xview)
ScrollbarY.config(command=student_table.yview)
student_table.config(show='headings')
student_table.pack()
top.mainloop()
