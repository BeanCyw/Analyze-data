"""Manage Product Data"""
from tkinter import *
from tkinter import messagebox
from Stock import set_pro

# Connecting to the database

# importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql


## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
global mydb
mydb = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "FWMsod25",
    database="ProductsDatabaseTest",
    buffered=True
)
global mycursor
mycursor = mydb.cursor()

def product():
    """Products Setting Windows"""
    product_win = Toplevel()
    product_win.title("Add Product Data")

    Label(product_win, text='จัดการสินค้า',font=("TH Sarabun New", 25),width=10, padx=1,pady=5).grid(row=0,column=1,columnspan=5)


    Label(product_win, text='ชื่อสินค้า',font=("TH Sarabun New", 16),width=10,anchor="e").grid(row=1,column=1,columnspan=1)
    name = Entry(product_win, width = 12,font=("TH Sarabun New", 14),bg='gray99')
    name.grid(row=1,column=2)
    
    Label(product_win, text='ประเภทสินค้า',font=("TH Sarabun New", 16),width=12,pady=10,anchor="e").grid(row=1,column=3)
    
    def pro_id_def():
        """Assign Products ID"""
        global pro_id
        pro_id = 0
        check_id = "SELECT * FROM products WHERE productsID=(SELECT MAX(productsId) FROM products)"
        mycursor.execute(check_id)
        myresult = mycursor.fetchone()
        if myresult == None:
            pro_id = 1
        else:
            pro_id = myresult[0]
            pro_id += 1

    pro_id_def()

    global new_category
    new_category = None
    
    clicked = StringVar()
    global category_options
    category_from_db = "SELECT * FROM products"
    mycursor.execute(category_from_db)
    category_data = mycursor.fetchall()
    if category_data == [] and new_category == None:
        category_options = ['ไม่พบประเภทสินค้า']
    else:
        category_options = [cate[2] for cate in category_data]

    clicked = StringVar()

    def update_category():
        """Update Category"""
        if new_cate.get() == "":
            messagebox.showerror("Error", "กรุณากรอกประเภทสินค้า")
        else:
            global new_category
            new_category = new_cate.get()
            set_cate()
            add_cate.destroy()

    def set_cate():
        """Show category setting"""
        global category_options
        category_from_db = "SELECT * FROM products "
        mycursor.execute(category_from_db)
        category_data = mycursor.fetchall()
        if category_data == [] and new_category == None:
            category_options = ['ไม่พบประเภทสินค้า']
        else:
            category_options = [cate[2] for cate in category_data]

        if new_category != None:
            category_options = set(category_options)
            category_options = list(category_options)
            category_options.insert(0, new_category)

        clicked = StringVar()
        category_show()
    
    def category_show():
        """Show all category"""
        global category_options
        category_shw = category_options
        category_options = set(category_options)
        category_options = list(category_options)
        clicked.set(category_shw[0])
        category = OptionMenu(product_win, clicked, *category_options)
        category.configure(width=15, justify=CENTER, font=("TH Sarabun New", 15),bg="gray30", fg="white",borderwidth=0)
        category['menu'].config(font=("TH Sarabun New", (15)),bg="gray30", fg="white")
        category.grid(row=1,column=4,columnspan=1,sticky='w')

    category_show()

    def add_category():
        """Add new category"""
        global add_cate
        add_cate = Toplevel()
        add_cate.title("AddCategory")
        Label(add_cate, text="เพิ่มประเภทสินค้า",font=("TH Sarabun New", 15)).pack(side=LEFT)
        global new_cate
        new_cate = Entry(add_cate, width=20,font=("TH Sarabun New", 15))
        new_cate.pack(side=LEFT)
        submit_add_cate = Button(add_cate, text='ยืนยัน', command=update_category,font=("TH Sarabun New", 15)).pack()
        

    def edit_cate_to_db(text):
        """Edit category to Database"""
        sql = "UPDATE products SET category = '" + e_cate.get() + "'WHERE category= '" + text + "'"
        mycursor.execute(sql)
        mydb.commit()
        edit_show.destroy()
        edit_cate.destroy()
        edit_catagory()
        set_cate()
        set_pro()
        

    def edit_cate_command():
        """Edit category information that you want to edit"""
        if listbox.get(ACTIVE) == "คลิกเลือกประเภทสินค้าที่จะแก้ไข  ":
            messagebox.showerror("Error", "กรุณาระบุสินค้าที่จะแก้ไข")
            edit_show.destroy()
            edit_catagory()

        else:
            global edit_cate
            edit_cate = Toplevel()
            edit_cate.title("Edit_cate")
            global e_cate
            Label(edit_cate, text="แก้ไขประเภทสินค้า",font=("TH Sarabun New", 15)).pack(side=LEFT)
            e_cate = Entry(edit_cate, width=20,font=("TH Sarabun New", 15))
            text = (listbox.get(ACTIVE)).lstrip(" ")
            e_cate.insert(0, text)
            e_cate.pack(side=LEFT)
            submit_edit_cate = Button(edit_cate, text='ยืนยัน', command=lambda : edit_cate_to_db(text,),font=("TH Sarabun New", 15)).pack()

    def edit_catagory():
        """Edit category Window"""
        global edit_show
        edit_show = Toplevel()
        edit_show.title("Edit")
        edit_show.geometry("500x300")
        scrollbar = Scrollbar(edit_show)
        scrollbar.pack(side=LEFT, fill=Y)

        global listbox
        listbox = Listbox(edit_show, yscrollcommand=scrollbar.set,font=("TH Sarabun New", 14))
        product_data = get_cate_form_db()
        number_of_pro= 0
        listbox.insert(END, "คลิกเลือกประเภทสินค้าที่จะแก้ไข  ")
        for data in set(product_data):
            number_of_pro+= 1
            cate_shw = "      %s"%(data)
            listbox.insert(END, cate_shw)
        listbox.pack(side=LEFT, fill=BOTH, expand=TRUE)
        Button(edit_show,text="แก้ไขประเภทสินค้า",command= edit_cate_command ,font=("TH Sarabun New", 14),bg='white',relief="raised",width=20,padx=1).pack()

        scrollbar.config(command=listbox.yview)

    def get_cate_form_db():
        """Get category data from Database"""
        product_from_db = "SELECT category FROM products "
        mycursor.execute(product_from_db)
        product_data = mycursor.fetchall()
        return product_data

    category_add_btn = Button(product_win,text="เพิ่ม",command= add_category ,font=("TH Sarabun New", 14),relief="raised",width=7,padx=1).grid(row=1,column=5,sticky='w')
    category_edit_btn = Button(product_win,text="แก้ไข",command= edit_catagory ,font=("TH Sarabun New", 14),relief="raised",width=7,padx=1).grid(row=1,column=6,sticky='e')
    
    Label(product_win, text='ราคาซื้อ',font=("TH Sarabun New", 16),width=10,anchor="e").grid(row=2,column=1,columnspan=1)
    buy = Entry(product_win, width = 12,font=("TH Sarabun New", 14),bg='gray99')
    buy.grid(row=2,column=2)
    Label(product_win, text='ราคาขาย',font=("TH Sarabun New", 16),width=12,anchor="e").grid(row=2,column=3,columnspan=1)
    sell = Entry(product_win, width = 15,font=("TH Sarabun New", 14),bg='gray99')
    sell.grid(row=2,column=4,sticky='w')
    

    def edit_pro_to_db(text):
        """Edit information of products that you want to Database"""
        if "รหัสสินค้า" in text:
            product_id_from_db = "SELECT productsId FROM products "
            mycursor.execute(product_id_from_db)
            product_data = mycursor.fetchall()

            for data in product_data:
                if int(e_pro.get()) == data[0]:
                    messagebox.showerror("Error", "มีรหัสสินค้านี้ในระบบอยู่แล้ว")
                    break
            else:
                text = text[27:]
                sql = "UPDATE products SET productsId = '" + e_pro.get() + "'WHERE productsId= '" + text + "'"
                mycursor.execute(sql)
                mydb.commit()
        elif "ชื่อสินค้า" in text:
            text = text[29:]
            sql = "UPDATE products SET productsName = '" + e_pro.get() + "'WHERE productsName= '" + text + "'"
            mycursor.execute(sql)
            mydb.commit()
        elif "ประเภทสินค้า" in text:
            text = text[26:]
            sql = "UPDATE products SET category = '" + e_pro.get() + "'WHERE category= '" + text + "'"
            mycursor.execute(sql)
            mydb.commit()
        elif "ราคาซื้อ" in text:
            text = text[28:]
            text = text.rstrip(" บาท")
            sql = "UPDATE products SET buy = '" + e_pro.get() + "'WHERE buy= '" + text + "'"
            mycursor.execute(sql)
            mydb.commit()
        elif "ราคาขาย" in text:
            text = text[26:]
            text = text.rstrip(" บาท")
            sql = "UPDATE products SET sell = '" + e_pro.get() + "'WHERE sells= '" + text + "'"
            mycursor.execute(sql)
            mydb.commit()

        products_showing.destroy()
        edit_pro.destroy()
        show_products()
        set_cate()
        pro_id_def()
        set_pro()


    
    def edit_pro_command():
        """Show product information that you want to edit"""
        text = listbox_pro.get(ACTIVE)
        if "สินค้าชิ้นที่  1" in text:
            messagebox.showerror("Error", "กรุณาคลิกเลือกข้อมูลที่ต้องการแก้ไข")
        else:
            global edit_pro
            edit_pro = Toplevel()
            edit_pro.title("Edit Products")
            global e_pro
            Label(edit_pro, text="แก้ไขสินค้า",font=("TH Sarabun New", 15)).pack(side=LEFT)
            e_pro = Entry(edit_pro, width=20,font=("TH Sarabun New", 15))
            if "รหัสสินค้า" in text:
                e_pro_id = Entry
                e_pro.insert(0, text[27:])
            elif "ชื่อสินค้า" in text:
                e_pro.insert(0, text[29:])
            elif "ประเภทสินค้า" in text:
                e_pro.insert(0, text[26:])
            elif "ราคาซื้อ" in text:
                text = text.rstrip(" บาท")
                e_pro.insert(0, text[28:])
            elif "ราคาขาย" in text:
                text = text.rstrip(" บาท")
                e_pro.insert(0, text[26:])
            e_pro.pack(side=LEFT)
            submit_edit_pro = Button(edit_pro, text='ยืนยัน', command=lambda : edit_pro_to_db(listbox_pro.get(ACTIVE)),font=("TH Sarabun New", 15)).pack()


    def delete_pro_from_db():
        """Delete product that you want from Database"""
        sql = "DELETE FROM products WHERE productsId='" + e_pro_delete.get() +"';"
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Info", "ลบสินค้าเรียบร้อย")
        delete_pro.destroy()
        products_showing.destroy()
        show_products()
        set_cate()
        pro_id_def()
        set_pro()
        


    def delete_pro_command():
        """Delete product that you want to delete"""
        text = listbox_pro.get(ACTIVE)
        if "รหัสสินค้า" in text:
            global delete_pro
            delete_pro = Toplevel()
            delete_pro.title("Edit Products")
            global e_pro_delete
            Label(delete_pro, text="ระบุรหัสสินค้า",font=("TH Sarabun New", 15)).pack(side=LEFT)
            e_pro_delete = Entry(delete_pro, width=20,font=("TH Sarabun New", 15))
            e_pro_delete_id = Entry
            e_pro_delete.insert(0, text[27:])
            e_pro_delete.pack(side=LEFT)
            submit_edit_pro = Button(delete_pro, text='ลบสินค้า', command=delete_pro_from_db,font=("TH Sarabun New", 15)).pack()
        else:
            messagebox.showerror("Error", "กรุณาระบุรหัสสินค้า")


    def show_products():
        """Show all information of products"""
        global products_showing
        products_showing = Toplevel()
        products_showing.title("Product Showing")
        products_showing.geometry("500x300")
        scrollbar = Scrollbar(products_showing)
        scrollbar.pack(side=LEFT, fill=Y)

        global listbox_pro
        listbox_pro = Listbox(products_showing, yscrollcommand=scrollbar.set,font=("TH Sarabun New", 14))
        product_from_db = "SELECT * FROM products "
        mycursor.execute(product_from_db)
        product_data = mycursor.fetchall()
        number_of_pro= 0
        for data in product_data:
            number_of_pro+= 1
            listbox_pro.insert(END, "  สินค้าชิ้นที่  " + str(number_of_pro))
            id_pro = "        รหัสสินค้า :       %d"%(data[0])
            name_pro = "        ชื่อสินค้า :         %s"%(data[1])
            cate_pro = "        ประเภทสินค้า :    %s"%(data[2])
            buy_pro = "        ราคาซื้อ :          %.2f"%(data[3]) + " บาท"
            sell_pro = "        ราคาขาย :         %.2f"%(data[4]) + " บาท"
            total = id_pro+name_pro+cate_pro+buy_pro+sell_pro
            listbox_pro.insert(END, id_pro)
            listbox_pro.insert(END, name_pro)
            listbox_pro.insert(END, cate_pro)
            listbox_pro.insert(END, buy_pro)
            listbox_pro.insert(END, sell_pro)
        listbox_pro.pack(side=LEFT, fill=BOTH, expand=TRUE)

        scrollbar.config(command=listbox_pro.yview)

        Button(products_showing,text="แก้ไขสินค้า",command= edit_pro_command ,font=("TH Sarabun New", 14),bg='white',relief="raised",width=20,padx=1).pack()
        Button(products_showing,text="ลบสินค้า",command= delete_pro_command ,font=("TH Sarabun New", 14),bg='white',relief="raised",width=20,padx=1).pack()


    def add_products():
        """Add new product & information about product"""
        global pro_id
        if name.get() == "":
            messagebox.showerror("Error", "กรุณาระบุข้อมูลสินค้า")
        else:
            sql = "INSERT INTO products (productsId, productsName, category, buy, sell, beforeSold, afterSold) VALUES (%s, %s, %s,%s ,%s, %s, %s)"
            val = (pro_id, name.get(), clicked.get() ,buy.get(), sell.get(), 0, 0)
            mycursor.execute(sql, val)
            mydb.commit()
            check_id = "SELECT * FROM products WHERE productsID=(SELECT MAX(productsId) FROM products)"
            mycursor.execute(check_id)
            myresult = mycursor.fetchone()
            pro_id == myresult[0]
            pro_id += 1
            name.delete(0, END)
            buy.delete(0, END)
            sell.delete(0, END)
            set_pro()
            

    products_show_btn = Button(product_win, text="แสดงสินค้า", command= show_products,font=("TH Sarabun New", 14),bg='steelblue2',relief="raised",width=15,padx=1).grid(row=3,column=2,columnspan=1)
    products_add_btn = Button(product_win, text="เพิ่มสินค้า", command= add_products ,font=("TH Sarabun New", 14),bg='goldenrod1',relief="raised",width=21,padx=1).grid(row=3,column=4,columnspan=1)

    product_win.mainloop()

