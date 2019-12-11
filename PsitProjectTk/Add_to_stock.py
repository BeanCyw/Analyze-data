from tkinter import *

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

def updateCategory():
        newCategory = newCate.get()
        global categoryOptions
        categoryFromDb = "SELECT * FROM products "
        mycursor.execute(categoryFromDb)
        categoryData = mycursor.fetchall()
        if categoryData == [] and newCategory == None:
            categoryOptions = ['None']
        else:
            categoryOptions = [cate[2] for cate in categoryData]

        if newCategory != None:
            categoryOptions.insert(0, newCategory)

        clicked = StringVar()
        categoryShow()

def categoryShow():
        global categoryOptions
        categoryOptions = set(categoryOptions)
        categoryOptions = list(categoryOptions)
        print(categoryOptions)
        clicked.set(categoryOptions[0])
        category = OptionMenu(productWin, clicked, *categoryOptions)
        category.configure(width=10, justify=CENTER, font=("Kanit", 13),fg='azure',bg='gray20',borderwidth=0)
        category.grid(row=1,column=4,columnspan=1,sticky='w')

def addCategory():
        addCate = Toplevel()
        addCate.title("AddCategory")
        Label(addCate, text="Add New Category",font=("Kanit", 13)).pack(side=LEFT)
        global newCate
        newCate = Entry(addCate, width=20,font=("Kanit", 13))
        newCate.pack(side=LEFT)
        submitAddCate = Button(addCate, text='Submit', command=updateCategory,font=("Kanit", 13)).pack()

def showProducts():
        productsShowing = Toplevel()
        productsShowing.title("Product Showing")
        numberofRow = 4
        Label(productsShowing, text='รหัสสินค้า',font=("Kanit", 16),width=10,borderwidth=1, relief="solid", padx=2, bg='gray70').grid(row=numberofRow,column=1)
        Label(productsShowing, text='ชื่อสินค้า',font=("Kanit", 16),width=10,borderwidth=1, relief="solid", padx=2,bg='gray70').grid(row=numberofRow,column=2)
        Label(productsShowing, text='ประเภทสินค้า',font=("Kanit", 16),width=12,borderwidth=1, relief="solid", padx=2,bg='gray70').grid(row=numberofRow,column=3)
        Label(productsShowing, text='ราคาซื้อ',font=("Kanit", 16),width=11,borderwidth=1, relief="solid", padx=10,bg='gray70').grid(row=numberofRow,column=4)
        Label(productsShowing, text='ราคาขาย',font=("Kanit", 16),width=15,borderwidth=1, relief="solid", padx=2,bg='gray70').grid(row=numberofRow,column=5)
        productFromDb = "SELECT * FROM products "
        mycursor.execute(categoryFromDb)
        productData = mycursor.fetchall()
        for data in productData:
            numberofRow += 1
            Label(productsShowing, text= data[0],font=("Kanit", 16),width=10,borderwidth=1, relief="solid", padx=2).grid(row=numberofRow,column=1)
            Label(productsShowing, text=data[1],font=("Kanit", 16),width=10,borderwidth=1, relief="solid", padx=2).grid(row=numberofRow,column=2)
            Label(productsShowing, text=data[2],font=("Kanit", 16),width=12,borderwidth=1, relief="solid", padx=2).grid(row=numberofRow,column=3)
            Label(productsShowing, text=("%.2f"%data[3]),font=("Kanit", 16),width=11,borderwidth=1, relief="solid", padx=10).grid(row=numberofRow,column=4)
            Label(productsShowing, text=("%.2f"%data[4]),font=("Kanit", 16),width=15,borderwidth=1, relief="solid", padx=2).grid(row=numberofRow,column=5)


def addProducts():
        global proId
        sql = "INSERT INTO products (productsId, productsName, category, buy, sell, beforeSold, afterSold) VALUES (%s, %s, %s,%s ,%s, %s, %s)"
        val = (proId, name.get(), clicked.get() ,buy.get(), sell.get(), 0, 0)
        mycursor.execute(sql, val)
        mydb.commit()
        checkId = "SELECT * FROM products WHERE productsID=(SELECT MAX(productsId) FROM products)"
        mycursor.execute(checkId)
        myresult = mycursor.fetchone()
        proId = myresult[0]
        proId = proId[:3] + str(int(proId[3])+1)
        print(proId, "Before")
        name.delete(0, END)
        buy.delete(0, END)
        sell.delete(0, END)