"""Manage Stock Data"""
from tkinter import *
from tkinter import messagebox
import AddProductsButton as apb

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

def stock():
    """stock windows"""
    mydb.commit()
    global stock_showing
    stock_showing = Toplevel()
    stock_showing.title("Stock Showing")
    stock_showing.geometry("800x600+500+150")
    global scrollbar
    scrollbar = Scrollbar(stock_showing)
    scrollbar.pack(side=LEFT, fill=Y)
    global listbox_stock
    listbox_stock = Listbox(stock_showing, yscrollcommand=scrollbar.set,font=("TH Sarabun New", 14+10))
    product_data = set_pro()
    number_of_pro = 0
    for data in product_data:
        number_of_pro+= 1
        listbox_stock.insert(END, "  สินค้าชิ้นที่  " + str(number_of_pro))
        id_pro = "        รหัสสินค้า :       %d"%(data[0])
        name_pro = "        ชื่อสินค้า :         %s"%(data[1])
        cate_pro = "        ประเภทสินค้า :    %s"%(data[2])
        after = "        จำนวนสินค้าในคลัง :      %d"%(data[6])
        listbox_stock.insert(END, id_pro)
        listbox_stock.insert(END, name_pro)
        listbox_stock.insert(END, cate_pro)
        listbox_stock.insert(END, after)
    listbox_stock.pack(side=LEFT, fill=BOTH, expand=TRUE)
    text = listbox_stock.get(ACTIVE)
    scrollbar.config(command=listbox_stock.yview)
    Label(stock_showing,text="คลังสินค้า",font=("TH Sarabun New", 24+10),width=10,padx=1).pack()

    Button(stock_showing,text="เพิ่มจำนวนสินค้าในคลัง",command=lambda : set_stock(True) ,font=("TH Sarabun New", 14+10),bg='white',relief="raised",width=20).pack()
    Button(stock_showing,text= "กำหนดจำนวนสินค้าในคลัง",command=lambda : set_stock(False) ,font=("TH Sarabun New", 14+10),bg='white',relief="raised",width=20).pack()

def set_pro():
    mydb.commit
    product_from_db = "SELECT * FROM products "
    mycursor.execute(product_from_db)
    product_data = mycursor.fetchall()
    print(product_data)
    print("do set pro func")
    return product_data
    
def stock_set_win_to_db(check_func):
    """set database"""
    if check_func:
        sql = "UPDATE products SET beforesold = afterSold + ' " + stock_quantity_entry.get() + "'WHERE productsId= '" + stock_id_entry.get() + "'"
        mycursor.execute(sql)
        mydb.commit()
        sql = "UPDATE products SET afterSold = afterSold + ' " + stock_quantity_entry.get() + "'WHERE productsId= '" + stock_id_entry.get() + "'"
        mycursor.execute(sql)
        mydb.commit()
        
        stock_showing.destroy()
        stock_set_win.destroy()
        stock()
    else:
        sql = "UPDATE products SET afterSold = ' " + stock_quantity_entry.get() + "'WHERE productsId= '" + stock_id_entry.get() + "'"
        mycursor.execute(sql)
        mydb.commit()
        sql = "UPDATE products SET beforesold = ' " + stock_quantity_entry.get() + "'WHERE productsId= '" + stock_id_entry.get() + "'"
        mycursor.execute(sql)
        mydb.commit()
        stock_showing.destroy()
        stock_set_win.destroy()
        stock()

def set_stock(check_func):
    """set stock in database"""
    global stock_set_win
    stock_set_win = Toplevel()
    stock_set_win.title("Set Stock")
    global stock_entry
    Label(stock_set_win, text="รหัสสินค้า",font=("TH Sarabun New", 15+10),anchor="e").grid(row=0,column=0)
    Label(stock_set_win, text="จำนวนที่ต้องการเพิ่ม",font=("TH Sarabun New", 15+10),anchor="w").grid(row=1,column=0)
    global stock_id_entry
    stock_id_entry = Entry(stock_set_win, width=20,font=("TH Sarabun New", 15+10))
    text = (listbox_stock.get(ACTIVE)).lstrip(" ")
    if "รหัสสินค้า" in text:
        stock_id_entry.insert(0, text[19:])
    global stock_quantity_entry
    stock_quantity_entry = Entry(stock_set_win, width=20,font=("TH Sarabun New", 15+10))
    stock_quantity_entry.grid(row=1,column=1)
    stock_id_entry.grid(row=0,column=1)
    submit_stock_set_id = Button(stock_set_win, text='ยืนยัน',command=lambda : stock_set_win_to_db(check_func) , font=("TH Sarabun New", 15+10), height=2, width=6).grid(row=0,column=2,rowspan=2)
