from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("Book Store and Management Account Services")

        self.root.withdraw()

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 3
        y = (self.root.winfo_screenheight() -
             self.root.winfo_reqheight()) / 4.5
        self.root.geometry("560x400+%d+%d" % (x, y))

        self.root.resizable(False, False)

        # Frame
        self.txt_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="#004040")
        self.txt_frame.place(x=0, y=0, width=560, height=400)

        # Frame for Buttons
        self.btn_frame = Frame(
            self.txt_frame, bd=2, relief=RIDGE, bg="#004040")
        self.btn_frame.place(x=45, y=35, width=466, height=330)

        # Login Form Button
        self.login_btn = Button(self.btn_frame, text='Login Form', width=40, height=3, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=self.login)
        self.login_btn.grid(row=1, column=5, pady=28, padx=23)

        # Register Form Button
        self.register_btn = Button(self.btn_frame, text='Register Form', width=40, height=3, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                   font=("roboto sans-serif", 13, "bold"), command=self.register)
        self.register_btn.grid(row=2, column=5)

        # Close Button
        self.close_btn = Button(self.btn_frame, text='Exit System', width=40, height=3, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=self.close)
        self.close_btn.grid(row=3, column=5, pady=28, padx=23)

    def close(self):
        ext = messagebox.askyesno(
                'Database', 'Do you want to this window ')

        if ext > 0:
            self.root.destroy()


    def login(self):

        top = Toplevel()
        top.title("Book Store and Management Login Employee Form")

        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 3
        y = (top.winfo_screenheight() -
             top.winfo_reqheight()) / 3.5
        top.geometry("560x362+%d+%d" % (x, y))

        top.resizable(False, False)
        #    Function Here

        def clear():
            top.username_entry.delete(0, END)
            top.password_entry.delete(0, END)

        def exit_form():
            top.destroy()


        def login_user():

            if top.username_entry.get() == '' or top.password_entry.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')
                clear()
            else:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="", database="gadget-store")
                    cur = con.cursor()
                    cur.execute("select * from account where username=%s and password=%s",(username_text.get(), password_text.get()))
                    row = cur.fetchone()

                    if row == None:
                        messagebox.showerror(
                            'Error', 'Undefined Username and Password, Please Try Again Later')
                        clear()
                    else:
                        messagebox.showinfo(
                            'Success', 'Welcome to Book Store Management System')
                        clear()
                        self.root.destroy()
                        import Form2
                    con.close()
                except Exception as es:
                    messagebox.showerror(
                        'Error', f'Error due to: {str(es)}')

        #    Design Here
        # Frames
        top.title_frame = Frame(
            top, bd=4, relief=RIDGE, bg="#004040")
        top.title_frame.place(x=0, y=0, width=560, height=326)

        # Title Head
        top.lbl_title = Label(
            top, text="Book Store Login Form", bd=4, relief=RIDGE,  bg="#004040", fg="#ffffff", font=("roboto sans-serif", 23), pady=14)
        top.lbl_title.pack(side=TOP, fill=X)

        # Form Frame
        top.form_frame = Frame(
            top, bd=4, relief=RIDGE, bg="#004040")
        top.form_frame.place(x=0, y=65, width=560, height=297)

        # Space to be Center lahat ng input build
        top.fname_label = Label(top.form_frame, text='',
                                font=('bold', 24), bg="#004040", fg="white", padx=20, pady=7).grid(row=2, column=2, sticky=W)
        # Username
        username_text = StringVar()
        top.username_label = Label(top.form_frame, text='Username :',
                                   font=("roboto sans-serif", 14), bg="#004040", fg="white", padx=5, pady=10).grid(
            row=3, column=3, sticky=W)
        top.username_entry = Entry(
            top.form_frame, textvariable=username_text, width=30, bd=5, font=("roboto sans-serif", 14))
        top.username_entry.grid(row=3, column=4)

        # Password
        password_text = StringVar()
        top.password_label = Label(top.form_frame, text='Password :',
                                   font=("roboto sans-serif", 14), bg="#004040", fg="white", padx=5, pady=14).grid(
            row=4, column=3, sticky=W)
        top.password_entry = Entry(
            top.form_frame, textvariable=password_text, width=30, bd=5, show="*", font=("roboto sans-serif", 14))
        top.password_entry.grid(row=4, column=4)

        # Buttons and Frame
        # Frame
        top.btn_frame = Frame(
            top.form_frame, bd=2, relief=RIDGE, bg="#004040")
        top.btn_frame.place(x=0, y=199, width=551, height=90)

        # Space Label para ma-move down
        top.space_lbl = Label(top.btn_frame, text='',
                              bg="#004040", padx=38,).grid(row=2, column=0)

        # Buttons
        top.login_btn = Button(top.btn_frame, text='Login Now', width=19, height=2,  bd=2,
                               relief=FLAT, bg="#005a5a", fg="white", font=("roboto sans-serif", 10, "bold"), command=login_user)
        top.login_btn.grid(row=2, column=1, padx=19, pady=23)

        top.close_btn = Button(top.btn_frame, text='Exit Now', width=19, height=2,
                              bg="#005a5a", fg="white", bd=2, relief=FLAT, font=("roboto sans-serif", 10, "bold"), command=exit_form)
        top.close_btn.grid(row=2, column=2)

    def register(self):

        top = Toplevel()
        top.title("Book Store and Management Registration Form")
        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 6.7
        y = (top.winfo_screenheight() -
             top.winfo_reqheight()) / 4.4
        top.geometry("985x420+%d+%d" % (x, y))
        top.resizable(False, False)

        # Function Here
        def clear():
            top.fname_entry.delete(0, END)
            top.lname_entry.delete(0, END)
            top.username_entry.delete(0, END)
            top.email_entry.delete(0, END)
            top.gender_entry.delete(0, END)
            top.address_entry.delete(0, END)
            top.password_entry.delete(0, END)
            top.cpassword_entry.delete(0, END)

        def exit_form():
            top.destroy()

        def register_acc():
            # error trap lng naman
            if fname_text.get() == '' or lname_text.get() == '' or username_text.get() == '' or email_text.get() == '' or gender_text.get() == '' or address_text.get() == '' or password_text.get() == '' or cpassword_text.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')
                clear()

            elif password_text.get() != cpassword_text.get():
                messagebox.showerror(
                    'Error', 'Password should be same of Confirm Password')

            else:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="", database="gadget-store")
                    cur = con.cursor()
                    cur.execute("select * from account where email=%s",
                                email_text.get())
                    row = cur.fetchone()

                    # pag may dati ka ng email na pinang-register di niya i aallow ung email dapat new
                    if row != None:
                        messagebox.showerror(
                            'Error', 'Your Email is Already Exist ')

                    # Para pumasok sa database
                    else:
                        cur.execute(
                            "insert into account (firstname,lastname,username,email,gender,address,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (fname_text.get(),
                             lname_text.get(),
                             username_text.get(),
                             email_text.get(),
                             gender_text.get(),
                             address_text.get(),
                             password_text.get()
                             ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Register Successfully")
                        clear()

                except Exception as es:
                    messagebox.showerror(
                        'Error', f'Error due to: {str(es)}')

        # Design

        # Title Head
        top.lbl_title = Label(
            top, text="Book Store Registration Form", bd=4, fg="white", relief=RIDGE,  bg="#005a5a", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frames
        top.title_frame = Frame(
            top, bd=4, relief=RIDGE, bg="#004040")
        top.title_frame.place(x=0, y=55, width=985, height=367)

        # Space to be Center lahat ng input build
        top.fname_label = Label(top.title_frame, text='',
                                font=('bold', 14), bg="#004040", fg="white", padx=12, pady=15).grid(
            row=2, column=2, sticky=W)

        # Firstname
        fname_text = StringVar()
        top.fname_label = Label(top.title_frame, text='First Name :',
                                font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10, pady=20).grid(
            row=2, column=3, sticky=W)

        top.fname_entry = Entry(
            top.title_frame, textvariable=fname_text, width=20, bd=3,
            font=("bold", 16))
        top.fname_entry.grid(row=2, column=4)

        # Last Name
        lname_text = StringVar()
        top.lname_label = Label(top.title_frame, text='Last Name :',
                                font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10).grid(
            row=2, column=5, sticky=W)
        top.lname_entry = Entry(
            top.title_frame, textvariable=lname_text, width=20, bd=3,
            font=("bold", 16))
        top.lname_entry.grid(row=2, column=6)

        # Username
        username_text = StringVar()
        top.username_label = Label(top.title_frame, text='Username :',
                                   font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10).grid(
            row=3, column=3, sticky=W)
        top.username_entry = Entry(
            top.title_frame, textvariable=username_text, width=20, bd=3,
            font=("bold", 16))
        top.username_entry.grid(row=3, column=4)

        # Email
        email_text = StringVar()
        top.email_label = Label(top.title_frame, text='Email :',
                                font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10).grid(
            row=3, column=5, sticky=W)
        top.email_entry = Entry(
            top.title_frame, textvariable=email_text, width=20, bd=3,
            font=("bold", 16))
        top.email_entry.grid(row=3, column=6)

        # Gender
        gender_text = StringVar()
        top.gender_label = Label(top.title_frame, text='Gender :',
                                 font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10, pady=20).grid(
            row=4, column=3, sticky=W)
        top.gender_entry = Entry(
            top.title_frame, textvariable=gender_text, width=20, bd=3,
            font=("bold", 16))
        top.gender_entry.grid(row=4, column=4)

        # Address
        address_text = StringVar()
        top.address_label = Label(top.title_frame, text='Address :',
                                  font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10, pady=20).grid(
            row=4, column=5, sticky=W)
        top.address_entry = Entry(
            top.title_frame, textvariable=address_text, width=20, bd=3,
            font=("bold", 16))
        top.address_entry.grid(row=4, column=6)

        # Password
        password_text = StringVar()
        top.password_label = Label(top.title_frame, text='Create Password :',
                                   font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10).grid(
            row=5, column=3, sticky=W)
        top.password_entry = Entry(
            top.title_frame, textvariable=password_text, width=20, bd=3, show="*",
            font=("bold", 16))
        top.password_entry.grid(row=5, column=4)

        # Confirm Password
        cpassword_text = StringVar()
        top.cpassword_label = Label(top.title_frame, text='Confirm Password :',
                                    font=("roboto sans-serif", 16), bg="#004040", fg="white", padx=10).grid(
            row=5, column=5, sticky=W)
        top.cpassword_entry = Entry(
            top.title_frame, textvariable=cpassword_text, width=20, bd=3, show="*",
            font=("bold", 16))
        top.cpassword_entry.grid(row=5, column=6)

        # Space to be Center lahat ng input build
        top.space_lbl = Label(top.title_frame, text='',
                              font=('bold', 16), bg="#004040", fg="white", padx=20).grid(
            row=8, column=6, sticky=W)

        # Frames para sa Buttons
        # Frames
        top.btn_frame = Frame(
            top.title_frame, bd=2, relief=RIDGE, bg="#004040")
        top.btn_frame.place(x=0, y=247, width=977, height=110)

        # Space Label para ma-move down
        top.space_lbl = Label(top.btn_frame, text='',
                              font=('bold', 14), bg="#004040", fg="white", padx=94).grid(
            row=1, column=2, sticky=W)

        # Buttons
        top.register_btn = Button(top.btn_frame, text='Register Now', width=25, height=2,  bd=2,
                                  relief=FLAT, bg="#005a5a", fg="white", font=("roboto sans-serif", 12, "bold"), command=register_acc)
        top.register_btn.grid(row=2, column=3, padx=19)

        top.close_btn = Button(top.btn_frame, text='Exit Now', width=25, height=2,
                              bg="#005a5a", fg="white", bd=2, relief=FLAT, font=("roboto sans-serif", 12, "bold"), command=exit_form)
        top.close_btn.grid(row=2, column=4)

        top.mainloop()


root = Tk()
obj = Login(root)
root.deiconify()
root.mainloop()
