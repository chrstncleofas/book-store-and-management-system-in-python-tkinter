from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Bookpage:
    def __init__(self, root):

        self.root = root
        self.root.title("Book Store and Management Dashboard")
        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 3
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 5
        self.root.geometry("590x424+%d+%d" % (x, y))
        self.root.resizable(False, False)

        # Frame
        self.txt_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="#004040")
        self.txt_frame.place(x=0, y=0, width=590, height=425)

        # Frame for Buttons
        self.btn_frame = Frame(
            self.txt_frame, bd=2, relief=RIDGE, bg="#004040")
        self.btn_frame.place(x=60, y=43, width=466, height=330)

        # Book Fields
        self.input_btn = Button(self.btn_frame, text='Book Store Input Fields', width=40, height=3, bd=2, relief=FLAT, bg="#005a5a", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=self.book_field)
        self.input_btn.grid(row=1, column=5, pady=28, padx=23)

        # Book Database
        self.view_btn = Button(self.btn_frame, text='Book Store Inventory & Database', width=40, height=3, bd=2, relief=FLAT, bg="#005a5a", fg="white",
                               font=("roboto sans-serif", 13, "bold"), command=self.book_database)
        self.view_btn.grid(row=2, column=5)

        # Close
        self.close_btn = Button(self.btn_frame, text='Exit Book Store System', width=40, height=3, bd=2, relief=FLAT, bg="#005a5a", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=self.close)
        self.close_btn.grid(row=3, column=5, pady=28, padx=23)


    def close(self):
        ext = messagebox.askyesno(
                'Database', 'Do you want to this window ')

        if ext > 0:
            self.root.destroy()


    def book_field(self):

        top = Toplevel()
        top.title("Book Store and Management System")
        
        x = (top.winfo_screenwidth() - top.winfo_reqwidth()) / 5
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 9
        top.geometry("890x564+%d+%d" % (x, y))
        top.resizable(False, False)

        # Function Here

        def clear():
            top.book_number_entry.delete(0, END)
            top.author_entry.delete(0, END)
            top.book_name_entry.delete(0, END)
            top.customer_entry.delete(0, END)
            top.date_entry.delete(0, END)
            top.price_entry.delete(0, END)
            top.amount_entry.delete(0, END)
            top.change_entry.delete(0, END)

        def compute():
            change_entry = (amount.get() - price.get())
            change.set(change_entry)

        def add_item():
            
            if book_number.get() == '' or author.get() == '' or book_name.get() == '' or customer.get() == '' or date.get() == '' or price.get() == '' or amount.get() == '' or change.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')
                return
            else:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="gadget-store")
                cur = con.cursor()

                cur.execute(
                    "insert into book (booknumber ,author, bookname, customername, date, price, amount, totalchange) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (book_number.get(),
                     author.get(),
                     book_name.get(),
                     customer.get(),
                     date.get(),
                     price.get(),
                     amount.get(),
                     change.get()
                     ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Adding Items Successfuly")
                clear()

        # Design Here
        # Head Label
        top.lbl_title = Label(
            top, text="Book Store and Management System", bd=4, fg="white", relief=RIDGE,  bg="#004040", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frame
        top.txt_frame = Frame(
            top, bd=4, relief=RIDGE, bg="#004040")
        top.txt_frame.place(x=0, y=55, width=890, height=509)
        # Space
        top.product_label = Label(top.txt_frame, text='',
                                  font=('', 14), pady=10, padx=20, bg="#004040", fg="white").grid(row=0, column=0, sticky=W)
        # Book Number
        book_number = StringVar()
        top.book_number_label = Label(top.txt_frame, text='Book Number :',
                                  font=('bold', 16), pady=10, padx=14, bg="#004040", fg="white").grid(row=1, column=0, sticky=W)
        top.book_number_entry = Entry(
            top.txt_frame, textvariable=book_number, width=20, bd=3, font=("bold", 16))
        top.book_number_entry.grid(row=1, column=1)

        # Author
        author = StringVar()
        top.author_label = Label(top.txt_frame, text='Author Name :', font=(
            'bold', 16), padx=10, bg="#004040", fg="white").grid(row=1, column=2, sticky=W)
        top.author_entry = Entry(top.txt_frame, textvariable=author,
                                   width=20, bd=3, font=("bold", 16))
        top.author_entry.grid(row=1, column=3)

        # Book Name
        book_name = StringVar()
        top.book_name_label = Label(top.txt_frame, text='Book Name :', font=(
            'bold', 16), padx=12, bg="#004040", fg="white").grid(row=2, column=0, sticky=W)
        top.book_name_entry = Entry(top.txt_frame, textvariable=book_name,
                                   width=20, bd=3, font=("bold", 16))
        top.book_name_entry.grid(row=2, column=1)

        # Customer Name
        customer = StringVar()
        top.customer_label = Label(top.txt_frame, text='Customer Name :', font=('bold', 16),
                                padx=10, bg="#004040", fg="white").grid(row=2, column=2, sticky=W)
        top.customer_entry = Entry(top.txt_frame, textvariable=customer,
                                width=20, bd=3, font=("bold", 16))
        top.customer_entry.grid(row=2, column=3)

        # Transaction
        date = StringVar()
        top.date_label = Label(top.txt_frame, text='Transact Date :', font=('bold', 16),
                               padx=10, pady=10, bg="#004040", fg="white").grid(row=3, column=0, sticky=W)
        top.date_entry = Entry(top.txt_frame, textvariable=date,
                               width=20, bd=3, font=("bold", 16))
        top.date_entry.grid(row=3, column=1)

        # Cost Frame
        top.cost_frame = Frame(
            top.txt_frame, bd=2, relief=RIDGE, bg="#004040")
        top.cost_frame.place(x=267, y=255, width=614, height=245)

        # Spacing
        top.space_label = Label(top.cost_frame, text='',
                    padx=110, pady=19, bg="#004040", fg="white").grid(row=1, column=0)

        # Book Price
        price = IntVar()
        top.price_label = Label(top.cost_frame, text='Book Price :', font=('bold', 16),
                            pady=10, bg="#004040", fg="white").grid(row=3, column=0)
        top.price_entry = Entry(top.cost_frame, textvariable=price,
                               width=27, bd=3, font=("bold", 16))
        top.price_entry.grid(row=3, column=1)
        
        # Amount
        amount = IntVar()
        top.amount_label = Label(top.cost_frame, text='Total Amount :', font=('bold', 16),
                               pady=10, bg="#004040", fg="white").grid(row=4, column=0)
        top.amount_entry = Entry(top.cost_frame, textvariable=amount,
                               width=27, bd=3, font=("bold", 16))
        top.amount_entry.grid(row=4, column=1)

        # Amount
        change = IntVar()
        top.change_label = Label(top.cost_frame, text='Total Change :', font=('bold', 16),
                               pady=10, bg="#004040", fg="white").grid(row=5, column=0)
        top.change_entry = Entry(top.cost_frame, textvariable=change,
                               width=27, bd=3, font=("bold", 16))
        top.change_entry.grid(row=5, column=1)


        # Frame for Buttons
        top.btn_frame = Frame(
            top.txt_frame, bd=2, relief=RIDGE, bg="#004040")
        top.btn_frame.place(x=0, y=255, width=263, height=245)

        # Button
        # Space
        top.space_lbl = Label(top.btn_frame, text='',
                              font=('bold', 14), bg="#004040", fg="white", padx=25).grid(
            row=1, column=1,sticky=W)

        top.add_btn = Button(top.btn_frame, text='Ok', width=20, height=2, bd=2, relief=FLAT, bg="#005a5a", fg="white",
                             font=("roboto sans-serif", 12, "bold"), command=add_item)
        top.add_btn.grid(row=2, column=1, padx=20)

        top.delete_btn = Button(top.btn_frame, text='Clear', width=20, height=2, bg="#005a5a", fg="white", bd=2, relief=FLAT,
                                font=("roboto sans-serif", 12, "bold"), command=clear)
        top.delete_btn.grid(row=3, column=1, pady=20)

        top.compute_btn = Button(top.btn_frame, text='Compute', width=20, height=2, bg="#005a5a", fg="white", bd=2, relief=FLAT,
                               font=("roboto sans-serif", 12, "bold"), command=compute)
        top.compute_btn.grid(row=4, column=1)


        top.mainloop()

    def book_database(self):
        top = Toplevel()
        top.title("Book Store and Management Database System")
        x = (top.winfo_screenwidth() -
             top.winfo_reqwidth()) / 10
        y = (top.winfo_screenheight() - top.winfo_reqheight()) / 30
        top.geometry("1130x665+%d+%d" % (x, y))
        top.resizable(False, False)


        # Funtion Here

        def populate_data():

            con = pymysql.connect(
                host="localhost", user="root", password="", database="gadget-store")
            cur = con.cursor()

            cur.execute("select * from book")
            rows = cur.fetchall()

            if len(rows) != 0:
                top.data_list.delete(*top.data_list.get_children())
                for row in rows:
                    top.data_list.insert('', END, values=row)
                con.commit()
            con.close()

        def select_item(ev):

            cursor_row = top.data_list.focus()
            contents = top.data_list.item(cursor_row)
            row = contents['values']
            book_number_text.set(row[0])
            author_text.set(row[1])
            book_name_text.set(row[2])
            customer_text.set(row[3])
            date_text.set(row[4])
            price_text.set(row[5])
            amount_text.set(row[6])
            change_text.set(row[7])

        def clear():
            top.book_number_entry.delete(0, END)
            top.author_entry.delete(0, END)
            top.book_name_entry.delete(0, END)
            top.customer_entry.delete(0, END)
            top.date_entry.delete(0, END)
            top.price_entry.delete(0, END)
            top.amount_entry.delete(0, END)
            top.change_entry.delete(0, END)

        def delete_item():
            con = pymysql.connect(
                host="localhost", user="root", password="", database="gadget-store")
            cur = con.cursor()
            cur.execute("delete from book where booknumber=%s", book_number_text.get())

            dlt = messagebox.askyesno(
                'Gadgets', 'Do you want to delete this file ')

            clear()
            con.commit()

            if dlt > 0:
                clear()
                populate_data()

            con.close()

        def update_item():
            con = pymysql.connect(
                host="localhost", user="root", password="", database="gadget-store")
            cur = con.cursor()
            cur.execute(
                "update book set booknumber=%s, author=%s, bookname=%s, customername=%s, date=%s, price=%s, amount=%s, totalchange=%s where book . booknumber=%s",
                (book_number_text.get(),
                 author_text.get(),
                 book_name_text.get(),
                 customer_text.get(),
                 date_text.get(),
                 price_text.get(),
                 amount_text.get(),
                 change_text.get(),
                 book_number_text.get()
                 ))
            con.commit()
            messagebox.showinfo("Success", "Update Successfuly")
            populate_data()
            clear()
            con.close()
            
        def close():
            ext = messagebox.askyesno(
                'Database', 'Do you want to this window ')

            if ext > 0:
                top.destroy()


        # Design Here

        # Head Label
        top.lbl_title = Label(
            top, text="Book Store and Management System", bd=4, fg="white", relief=RIDGE,  bg="#004040", font=("roboto sans-serif", 23), pady=7)
        top.lbl_title.pack(side=TOP, fill=X)

        # Frame Table
        top.detail_frame = Frame(
            top, bd=4, relief=RIDGE, bg="#004040")
        top.detail_frame.place(x=0, y=390, width=1130, height=276)

        # Frame Input
        top.txt_frame = Frame(
            top, bd=4, relief=RIDGE, bg="#004040")
        top.txt_frame.place(x=0, y=55, width=1130, height=340)

        # Buttons Frame
        top.btn_frame = Frame(
            top.detail_frame, bd=3, relief=RIDGE, bg="#004040")
        top.btn_frame.place(x=0, y=170, width=1122, height=98)

        # Button Here
        # Space for Buttons
        top.space_label = Label(top.btn_frame, text='',
                                font=('', 10), bg="#004040", fg="white").grid(row=1, column=2, pady=20, padx=5)
        # Edit
        top.edit_btn = Button(top.btn_frame, text='Change', width=24, height=2, bd=2, relief=FLAT, bg="#005a5a", fg="white",
                              font=("roboto sans-serif", 13, "bold"), command=update_item)
        top.edit_btn.grid(row=1, column=3, pady=20, padx=10)

        # Delete
        top.delete_btn = Button(top.btn_frame, text='Delete', width=24, height=2, bd=2, relief=FLAT, bg="#005a5a", fg="white",
                                font=("roboto sans-serif", 13, "bold"), command=delete_item)
        top.delete_btn.grid(row=1, column=4, pady=20, padx=10)

        # Back
        top.bck_btn = Button(top.btn_frame, text='Clear', width=24, height=2, bg="#005a5a", fg="white", bd=2, relief=FLAT,
                             font=("roboto sans-serif", 13, "bold"), command=clear)
        top.bck_btn.grid(row=1, column=5, padx=12)

        # Exit
        top.exit_btn = Button(top.btn_frame, text='Exit', width=24, height=2, bg="#005a5a", fg="white", bd=2, relief=FLAT,
                              font=("roboto sans-serif", 13, "bold"), command=close)
        top.exit_btn.grid(row=1, column=6, padx=12)

        # Cost Area 
        top.cost_frame = Frame(
            top.txt_frame, bd=3, relief=RIDGE, bg="#004040")
        top.cost_frame.place(x=580, y=40, width=522, height=235)

        # Space
        top.space_label = Label(top.cost_frame, text='',
                                font=('', 10), bg="#004040", fg="white").grid(row=0, column=2, sticky=W, padx=43)

        # Price
        price_text = StringVar()
        top.book_number_label = Label(top.cost_frame, text='Total Price :',
                             font=('bold', 14), bg="#004040", fg="white").grid(row=1, column=0, sticky=W, padx=35, pady=20)
        top.price_entry = Entry(
            top.cost_frame, textvariable=price_text, width=25, bd=3, font=("bold", 15))
        top.price_entry.grid(row=1, column=1)

        # Amount
        amount_text = StringVar()
        top.amount_label = Label(top.cost_frame, text='Total Amount :',
                             font=('bold', 14), bg="#004040", fg="white").grid(row=2, column=0, sticky=W, padx=35)
        top.amount_entry = Entry(
            top.cost_frame, textvariable=amount_text, width=25, bd=3, font=("bold", 15))
        top.amount_entry.grid(row=2, column=1)

        # Change
        change_text = StringVar()
        top.change_label = Label(top.cost_frame, text='Total Change :',
                             font=('bold', 14), bg="#004040", fg="white").grid(row=3, column=0, sticky=W, padx=35, pady=20)
        top.change_entry = Entry(
            top.cost_frame, textvariable=change_text, width=25, bd=3, font=("bold", 15))
        top.change_entry.grid(row=3, column=1)

        # Space
        top.space_label = Label(top.txt_frame, text='',
                                font=('', 10), bg="#004040", fg="white").grid(row=0, column=2, sticky=W, padx=43)
        # Book Number
        book_number_text = StringVar()
        top.book_number_label = Label(top.txt_frame, text='Book Number :',
                             font=('bold', 14), bg="#004040", fg="white").grid(row=1, column=0, sticky=W, padx=55, pady=20)
        top.book_number_entry = Entry(
            top.txt_frame, textvariable=book_number_text, width=25, bd=3, font=("bold", 15))
        top.book_number_entry.grid(row=1, column=1)

        # Book Name
        book_name_text = StringVar()
        top.book_name_label = Label(top.txt_frame, text='Book Name :',
                                  font=('bold', 14), bg="#004040", fg="white").grid(row=2, column=0, sticky=W, padx=52)
        top.book_name_entry = Entry(
            top.txt_frame, textvariable=book_name_text, width=25, bd=3, font=("bold", 15))
        top.book_name_entry.grid(row=2, column=1)

        # Author
        author_text = StringVar()
        top.author_label = Label(top.txt_frame, text='Author Name :', font=(
            'bold', 14), bg="#004040", fg="white").grid(row=4, column=0, sticky=W, padx=50)
        top.author_entry = Entry(top.txt_frame, textvariable=author_text,
                                   width=25, bd=3, font=("bold", 15))
        top.author_entry.grid(row=4, column=1)

        # Transaction Date
        date_text = StringVar()
        top.date_label = Label(top.txt_frame, text='Transact Date :', font=(
            'bold', 14), bg="#004040", fg="white").grid(row=3, column=0, sticky=W, padx=50, pady=20)
        top.date_entry = Entry(top.txt_frame, textvariable=date_text,
                                   width=25, bd=3, font=("bold", 15))
        top.date_entry.grid(row=3, column=1)

        # Customer Name
        customer_text = StringVar()
        top.customer_label = Label(top.txt_frame, text='Customer Name :', font=('bold', 14),
                                bg="#004040", fg="white").grid(row=5, column=-0, sticky=W, padx=50,pady=20)
        top.customer_entry = Entry(top.txt_frame, textvariable=customer_text,
                                width=25, bd=3, font=("bold", 15))
        top.customer_entry.grid(row=5, column=1)

        # Listbox Frame
        top.list_frame = Frame(
            top.detail_frame, bd=2, relief=RIDGE, bg="#004040")
        top.list_frame.place(x=0, y=0, width=1122, height=170)

        # Treeview Scrollbar
        scroll_x = Scrollbar(top.list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(top.list_frame, orient=VERTICAL)

        # Treeview
        top.data_list = ttk.Treeview(top.list_frame, height=12, columns=(
            "booknumber", "author", "bookname", "customer", "date", "price", "amount", "change"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        top.data_list.configure(yscrollcommand=scroll_x.set)
        scroll_x.configure(command=top.data_list.xview)

        top.data_list.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=top.data_list.yview)

        top.data_list.heading("booknumber", text="Book No.")
        top.data_list.heading("author", text="Author Name")
        top.data_list.heading("bookname", text="Book Name")
        top.data_list.heading("customer", text="Customer Name")
        top.data_list.heading("date", text="Date")
        top.data_list.heading("price", text="Total Price")
        top.data_list.heading("amount", text="Total Amount")
        top.data_list.heading("change", text="Total Change")

        top.data_list['show'] = 'headings'

        top.data_list.column("booknumber", width=30)
        top.data_list.column("author", width=70)
        top.data_list.column("bookname", width=100)
        top.data_list.column("customer", width=160)
        top.data_list.column("date", width=46)
        top.data_list.column("price", width=42)
        top.data_list.column("amount", width=45)
        top.data_list.column("change", width=43)


        top.data_list.pack(fill=BOTH, expand=1)

        top.data_list.bind('<ButtonRelease-1>', select_item)

        populate_data()

        top.mainloop()


root = Tk()
obj = Bookpage(root)
root.deiconify()
root.mainloop()