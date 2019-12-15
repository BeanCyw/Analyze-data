"""Manage Selling"""
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

global mydb
mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="FWMsod25",
    database="ProductsDatabaseTest",
    buffered=True
)
global mycursor
mycursor = mydb.cursor()


def selling():
    """selling windows"""
    mydb.commit()
    global selling_showing
    selling_showing = Toplevel()
    selling_showing.title("Selling Showing")
    selling_showing.geometry("800x700+400+60")
    basket_show()
    Label(selling_showing, text="เลือกประเภทสินค้า",
          font=("TH Sarabun New", 24+10), width=15, padx=1).pack()
    category_show()
    submit_button = Button(selling_showing, text='ยืนยัน', command=lambda:
                           product_show(), font=("TH Sarabun New", 15+10),
                           width=19)
    submit_button.pack()
    Label(selling_showing, text="", font=("TH Sarabun New", 15+10),
          width=15).pack()
    Label(selling_showing, text=" ราคารวม", font=("TH Sarabun New", 18+10),
          width=21, justify=LEFT, anchor=W).pack()

    Label(selling_showing, text="  %.2f  บาท" % (price),
          font=("TH Sarabun New", 15+10), width=23, justify=LEFT,
          anchor=NW).pack()
    Label(selling_showing, text="", font=("TH Sarabun New", 15+10),
          width=15).pack()
    delete_button = Button(selling_showing, text='ลบสินค้า',
                           command=delete_from_basket,
                           font=("TH Sarabun New", 15+10), width=19)
    delete_button.pack()
    success_button = Button(selling_showing, text='ทำรายการเสร็จสิ้น',
                            command=finish_sell,
                            font=("TH Sarabun New", 15+10), width=19)
    success_button.pack()


def product_show():
    """show product in some categories that you have choose"""
    mydb.commit()
    global product_showing
    product_showing = Toplevel()
    product_showing.title("Product Showing")
    product_showing.geometry("800x500+450+60")
    scrollbar = Scrollbar(product_showing)
    scrollbar.pack(side=RIGHT, fill=Y)
    Label(product_showing, text="คลิกรหัสสินค้าเพื่อเลือก",
          font=("TH Sarabun New", 20+10),
          width=20, padx=1, anchor=W).pack()

    global listbox_to_basket
    listbox_to_basket = Listbox(product_showing,
                                yscrollcommand=scrollbar.set,
                                font=("TH Sarabun New", 14+10))
    product_from_db = "SELECT * FROM products WHERE category='" + \
        clicked.get() + "'"
    mycursor.execute(product_from_db)
    product_data = mycursor.fetchall()
    number_of_pro = 0
    for data in product_data:
        number_of_pro += 1
        listbox_to_basket.insert(END, "  สินค้าชิ้นที่  " + str(number_of_pro))
        id_pro = "        รหัสสินค้า :       %d" % (data[0])
        name_pro = "        ชื่อสินค้า :         %s" % (data[1])
        sell_pro = "        ราคาขาย :         %.2f" % (data[4]) + " บาท"
        after = "        จำนวนสินค้าในคลัง :      %d" % (data[6])
        listbox_to_basket.insert(END, id_pro)
        listbox_to_basket.insert(END, name_pro)
        listbox_to_basket.insert(END, sell_pro)
        listbox_to_basket.insert(END, after)
    listbox_to_basket.pack(side=LEFT, fill=BOTH, expand=TRUE)

    scrollbar.config(command=listbox_to_basket.yview)

    Label(product_showing, text="ระบุจำนวน", font=("TH Sarabun New", 16+10),
          width=15, padx=1).pack()
    global quantity_entry
    quantity_entry = Entry(product_showing, width=15,
                           font=("TH Sarabun New", 15+10))
    quantity_entry.pack()
    Button(product_showing, text="เพิ่มลงตะกร้า", command=set_basket,
           font=("TH Sarabun New", 14+10), relief="raised", width=20,
           padx=1).pack()


def category_show():
    """Show all category"""
    mydb.commit()
    global new_category
    new_category = None

    global clicked
    clicked = StringVar()
    global category_options
    category_from_db = "SELECT * FROM products"
    mycursor.execute(category_from_db)
    category_data = mycursor.fetchall()
    if category_data == [] and new_category is None:
        category_options = ['ไม่พบประเภทสินค้า']
    else:
        category_options = [cate[2] for cate in category_data]

    category_shw = category_options
    category_options = set(category_options)
    category_options = list(category_options)
    clicked.set(category_shw[0])
    category = OptionMenu(selling_showing, clicked, *category_options)
    category.configure(width=15, justify=CENTER,
                       font=("TH Sarabun New", 15+10), bg="gray30",
                       fg="white", borderwidth=0)
    category['menu'].config(font=("TH Sarabun New", (15+10)), bg="gray30",
                            fg="white")
    category.pack()
    mydb.commit()


def basket_show():
    """show basket"""
    mydb.commit()
    scrollbar = Scrollbar(selling_showing)
    scrollbar.pack(side=LEFT, fill=Y)

    global listbox_pro
    listbox_pro = Listbox(selling_showing, yscrollcommand=scrollbar.set,
                          font=("TH Sarabun New", 15+10))
    global basket
    check = "SELECT * FROM basket"
    mycursor.execute(check)
    basket = mycursor.fetchall()
    number_of_pro = 0
    global price
    price = 0
    if basket is None:
        listbox_pro.insert(END, "  ไม่มีสินค้าในตะกร้า ")
        listbox_pro.pack(side=LEFT, fill=BOTH, expand=TRUE)
    else:
        for data in basket:
            number_of_pro += 1
            check_as = "SELECT aftersold FROM products WHERE productsId = " + \
                str(data[0])
            mycursor.execute(check_as)
            after_sold_from_pro = mycursor.fetchall()
            listbox_pro.insert(END, "  สินค้าลำดับที่  " + str(number_of_pro))
            id_pro = "        รหัสสินค้า :       %d" % (data[0])
            name_pro = "        ชื่อสินค้า :         %s" % (data[1])
            sell_pro = "        ราคาขาย :         %.2f" % (data[3]) + " บาท"
            after = "        จำนวนสินค้าในคลัง :      %d" % \
                (after_sold_from_pro[0][0])
            quantity = "        จำนวนสั่งซื้อ :      %d" % (data[5])
            price_shw = "        ราคา :      %.2f" % (data[3]*data[5]) + " บาท"
            price += data[3]*data[5]
            listbox_pro.insert(END, id_pro)
            listbox_pro.insert(END, name_pro)
            listbox_pro.insert(END, sell_pro)
            listbox_pro.insert(END, after)
            listbox_pro.insert(END, quantity)
            listbox_pro.insert(END, price_shw)
        listbox_pro.pack(side=LEFT, fill=BOTH, expand=TRUE)

    scrollbar.config(command=listbox_pro.yview)


def set_basket():
    """Seet Basket"""
    text = listbox_to_basket.get(ACTIVE)
    mydb.commit()
    if "รหัสสินค้า" not in text:
        messagebox.showerror("Error",
                             "กรุณาคลิกเลือกรหัสสินค้าก่อนเพิ่มลงตะกร้า")
    elif quantity_entry.get().isnumeric() is False:
        messagebox.showerror("Error", "กรุณาใส่จำนวนสินค้าให้ถูกต้อง")
    else:
        text = text[27:]
        stock_check = "SELECT afterSold FROM products WHERE productsId = '" + \
            text + "'"
        mycursor.execute(stock_check)
        pro_in_stock = mycursor.fetchall()
        stock_check = "SELECT quantityPro FROM basket WHERE productId = '" + \
            text + "'"
        mycursor.execute(stock_check)
        quantity_in_basket = mycursor.fetchall()
        qtt_of_this_pro = 0
        for qtt in quantity_in_basket:
            qtt_of_this_pro += qtt[0]
        if (int(quantity_entry.get()) > pro_in_stock[0][0]) or \
           ((int(quantity_entry.get())+qtt_of_this_pro) > pro_in_stock[0][0]):
            messagebox.showerror("Error", "จำนวนสินค้าในคลัง ไม่เพียงพอ")
        else:
            check = "SELECT * FROM products WHERE productsId='" + text + "'"
            mycursor.execute(check)
            data_to_basket = mycursor.fetchall()

            check_id_basket = "SELECT productId FROM basket"
            mycursor.execute(check_id_basket)
            id_basket = mycursor.fetchall()
            for id_bas in id_basket:
                if id_bas[0] == int(text):
                    sql = "UPDATE basket SET quantityPro = quantityPro + " + \
                        quantity_entry.get() + ""
                    mycursor.execute(sql)
                    mydb.commit()
                    selling_showing.destroy()
                    quantity_entry.delete(0, END)
                    product_showing.destroy()
                    selling()
            else:
                sql = "INSERT INTO basket (productId, productName, category, \
                    sell, afterSold, quantityPro) \
                        VALUES (%s, %s, %s,%s ,%s, %s)"
                val = (data_to_basket[0][0], data_to_basket[0][1],
                       data_to_basket[0][2], data_to_basket[0][4],
                       data_to_basket[0][6], int(quantity_entry.get()))
                mycursor.execute(sql, val)
                mydb.commit()
                selling_showing.destroy()
                quantity_entry.delete(0, END)
                product_showing.destroy()
                selling()


def finish_sell():
    """finish sell"""
    mydb.commit()
    if basket == []:
        messagebox.showwarning("Warning", "ไม่พบสินค้าในตะกร้า")
    else:
        for data in basket:
            sql = "UPDATE products SET afterSold = afterSold - ' " + \
                str(data[5]) + "'WHERE productsId= '" + str(data[0]) + "'"
            mycursor.execute(sql)
            mydb.commit()
        sql = "DELETE FROM basket"
        mycursor.execute(sql)
        messagebox.showinfo("Success", "ทำรายการเสร็จสิ้น")
        selling_showing.destroy()
        selling()
        mydb.commit()


def delete_from_basket():
    """Edit Quantity"""
    del_text = listbox_pro.get(ACTIVE)
    if "รหัสสินค้า" not in del_text:
        messagebox.showerror("Error", "กรุณาคลิกรหัสสินค้าที่จะลบจากตะกร้า")
    else:
        response = messagebox.askokcancel("Confirm",
                                          "ต้องการลบสินค้าชิ้นนี้\
                                           จากตะกร้าหรือไม่ ?")
        if response == 1:
            del_text = del_text[27:]
            sql = "DELETE FROM basket WHERE productId = " + del_text
            mycursor.execute(sql)
            messagebox.showinfo("Success", "ลบสินค้าจากตะกร้าเสร็จสิ้น")
            selling_showing.destroy()
            selling()
            mydb.commit()
        else:
            pass
