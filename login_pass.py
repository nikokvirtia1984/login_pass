from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry('300x500')
root.title('System login')


def reg():
    text = Label(text='Please register to login')
    text_login = Label(text='Enter your login:')
    register_login = Entry()
    text_pass1 = Label(text='Enter your password:')
    register_pass1 = Entry()
    text_pass2 = Label(text='Enter password one more time:')
    register_pass2 = Entry()
    button_register = Button(text='Registration', command=lambda: save())
    text.pack()
    text_login.pack()
    register_login.pack()
    text_pass1.pack()
    register_pass1.pack()
    text_pass2.pack()
    register_pass2.pack()
    button_register.pack()

    def save():
        login_pass_save = {}
        login_pass_save[register_login.get()] = register_pass1.get()
        f = open('login.txt', 'wb')
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text='You are now registered, please login')
    text_enter_login = Label(text='Enter your login:')
    enter_login = Entry()
    text_enter_pass = Label(text='Enter your pass:')
    enter_pass = Entry(show='*')
    button_enter = Button(text='Enter', command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_pass.pack()
    button_enter.pack()

    def log_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo('access granted', 'you have 5 new messages')
            else:
                messagebox.showerror('access denied', 'you entered wrong login or password')
        else:
            messagebox.showerror('access denied', 'you entered wrong login')


reg()

root.mainloop()
