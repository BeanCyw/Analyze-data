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


# sql = "DROP TABLE Products"
# mycursor.execute(sql)
# mydb.commit()



def product():
    """Products Setting Windows"""
    productWin = Tk()
    productWin.title("Grocery Store")
    productWin.configure(background='gray20')

    Label(productWin, text='Add Product',font=("Kanit", 25),width=10, padx=1,pady=5,fg='goldenrod1',bg='gray20').grid(row=0,column=1,columnspan=5)


    Label(productWin, text='ชื่อสินค้า',font=("Kanit", 16),width=10,fg='azure',bg='gray20',anchor="e").grid(row=1,column=1,columnspan=1)
    name = Entry(productWin, width = 12,font=("Kanit", 12),fg='gray1',bg='gray99')
    name.grid(row=1,column=2)
    
    Label(productWin, text='ประเภทสินค้า',font=("Kanit", 16),width=12,fg='azure',bg='gray20',pady=10,anchor="e").grid(row=1,column=3)
    
    global newCategory
    newCategory = None
    
    clicked = StringVar()
    global categoryOptions
    categoryFromDb = "SELECT * FROM products"
    mycursor.execute(categoryFromDb)
    categoryData = mycursor.fetchall()
    # print(categoryData)
    if categoryData == [] and newCategory == None:
        categoryOptions = ['None']
    else:
        categoryOptions = [cate[2] for cate in categoryData]

    clicked = StringVar()

    def updateCategory():
        global newCategory
        newCategory = newCate.get()
        set_cate()
        addCate.destroy()

    def set_cate():
        global categoryOptions
        categoryFromDb = "SELECT * FROM products "
        mycursor.execute(categoryFromDb)
        categoryData = mycursor.fetchall()
        if categoryData == [] and newCategory == None:
            categoryOptions = ['None']
        else:
            categoryOptions = [cate[2] for cate in categoryData]

        if newCategory != None:
            categoryOptions = set(categoryOptions)
            categoryOptions = list(categoryOptions)
            categoryOptions.insert(0, newCategory)

        print(categoryOptions)
        clicked = StringVar()
        categoryShow()
    
    def categoryShow():
        global categoryOptions
        category_shw = categoryOptions
        categoryOptions = set(categoryOptions)
        categoryOptions = list(categoryOptions)
        clicked.set(category_shw[0])
        category = OptionMenu(productWin, clicked, *categoryOptions)
        category.configure(width=10, justify=CENTER, font=("Kanit", 13),fg='azure',bg='gray20',borderwidth=0)
        category.grid(row=1,column=4,columnspan=1,sticky='w')

    categoryShow()

    def addCategory():
        global addCate
        addCate = Toplevel()
        addCate.title("AddCategory")
        Label(addCate, text="Add New Category",font=("Kanit", 13)).pack(side=LEFT)
        global newCate
        newCate = Entry(addCate, width=20,font=("Kanit", 13))
        newCate.pack(side=LEFT)
        submitAddCate = Button(addCate, text='Submit', command=updateCategory,font=("Kanit", 13)).pack()

    def edit_cate_to_db(text):
        sql = "UPDATE products SET category = '" + eCate.get() + "'WHERE category= '" + text + "'"
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        edit_show.destroy()
        edit_cate.destroy()
        edit_catagory()
        set_cate()

    def edit_cate_command():
        global edit_cate
        edit_cate = Toplevel()
        edit_cate.title("Edit_cate")
        global eCate
        Label(edit_cate, text="Edit Category",font=("Kanit", 13)).pack(side=LEFT)
        eCate = Entry(edit_cate, width=20,font=("Kanit", 13))
        text = (listbox.get(ACTIVE)).lstrip(" ")
        eCate.insert(0, text)
        eCate.pack(side=LEFT)
        submitEditCate = Button(edit_cate, text='Submit', command=lambda : edit_cate_to_db(text,),font=("Kanit", 13)).pack()

    def edit_catagory():
        global edit_show
        edit_show = Toplevel()
        edit_show.title("Edit")
        edit_show.geometry("500x300")
        list_cate_shw()
        
    def list_cate_shw():
        scrollbar = Scrollbar(edit_show)
        scrollbar.pack(side=RIGHT, fill=Y)

        global listbox
        listbox = Listbox(edit_show, yscrollcommand=scrollbar.set,font=("Kanit", 12))
        productData = get_cate_form_db()
        number_of_pro= 0
        listbox.insert(END, "คลิกเลือกประเภทสินค้าที่จะแก้ไข  ")
        for data in set(productData):
            number_of_pro+= 1
            cate_shw = "      %s"%(data)
            # listbox.insert(END, "  ประเภทสินค้าที่  " + str(number_of_pro))
            listbox.insert(END, cate_shw)
        listbox.pack(side=LEFT, fill=BOTH, expand=TRUE)
        Button(edit_show,text="แก้ไขประเภทสินค้า",command= edit_cate_command ,font=("Kanit", 12),bg='white',fg='gray20',relief="raised",width=20,padx=1).pack()

        scrollbar.config(command=listbox.yview)

    def get_cate_form_db():
        productFromDb = "SELECT category FROM products "
        mycursor.execute(productFromDb)
        productData = mycursor.fetchall()
        return productData

    categoryAddBtn = Button(productWin,text="ADD",command= addCategory ,font=("Kanit", 12),bg='gray20',fg='green2',relief="raised",width=7,padx=1).grid(row=1,column=5,sticky='w')
    categoryEditBtn = Button(productWin,text="EDIT",command= edit_catagory ,font=("Kanit", 12),bg='gray20',fg='steelblue1',relief="raised",width=7,padx=1).grid(row=1,column=6,sticky='e')
    
    Label(productWin, text='ราคาซื้อ',font=("Kanit", 16),width=10,fg='azure',bg='gray20',anchor="e").grid(row=2,column=1,columnspan=1)
    buy = Entry(productWin, width = 12,font=("Kanit", 12),fg='gray1',bg='gray99')
    buy.grid(row=2,column=2)
    Label(productWin, text='ราคาขาย',font=("Kanit", 16),width=12,fg='azure',bg='gray20',anchor="e").grid(row=2,column=3,columnspan=1)
    sell = Entry(productWin, width = 15,font=("Kanit", 12),fg='gray1',bg='gray99')
    sell.grid(row=2,column=4,sticky='w')
    
    
    def showProducts():
        productsShowing = Toplevel()
        productsShowing.title("Product Showing")
        categoryFromDb = "SELECT productsName FROM products "
        mycursor.execute(categoryFromDb)
        nameData = mycursor.fetchall()
        global nameShow
        productsShowing.geometry("300x300")
        scrollbar = Scrollbar(productsShowing)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(productsShowing, yscrollcommand=scrollbar.set,font=("Kanit", 12))
        productFromDb = "SELECT * FROM products "
        mycursor.execute(productFromDb)
        productData = mycursor.fetchall()
        number_of_pro= 0
        for data in productData:
            number_of_pro+= 1
            listbox.insert(END, "  สินค้าชิ้นที่  " + str(number_of_pro))
            id_pro = "        รหัสสินค้า :       %d"%(data[0])
            name_pro = "        ชื่อสินค้า :         %s"%(data[1])
            cate_pro = "        ประเภทสินค้า :    %s"%(data[2])
            buy_pro = "        ราคาซื้อ :          %.2f"%(data[3])
            sell_pro = "        ราคาขาย :         %.2f"%(data[4])
            total = id_pro+name_pro+cate_pro+buy_pro+sell_pro
            listbox.insert(END, id_pro)
            listbox.insert(END, name_pro)
            listbox.insert(END, cate_pro)
            listbox.insert(END, buy_pro)
            listbox.insert(END, sell_pro)
        listbox.pack(side=LEFT, fill=BOTH, expand=TRUE)

        scrollbar.config(command=listbox.yview)
   
        

    checkId = "SELECT * FROM products WHERE productsID=(SELECT MAX(productsId) FROM products)"
    mycursor.execute(checkId)
    myresult = mycursor.fetchone()

    global proId
    proId = 0
    print(myresult)
    if myresult == None:
        proId = 1
    else:
        proId = myresult[0]
        proId += 1
        # proIdCheck = len(proId.lstrip("0"))
        # # print(proIdCheck, proId.lstrip("0"))
        # proId = proId[:3] + str(int(proId[3])+1)
        print(myresult[0])
        print(proId)

    def addProducts():
        global proId
        sql = "INSERT INTO products (productsId, productsName, category, buy, sell, beforeSold, afterSold) VALUES (%s, %s, %s,%s ,%s, %s, %s)"
        val = (proId, name.get(), clicked.get() ,buy.get(), sell.get(), 0, 0)
        mycursor.execute(sql, val)
        mydb.commit()
        checkId = "SELECT * FROM products WHERE productsID=(SELECT MAX(productsId) FROM products)"
        mycursor.execute(checkId)
        myresult = mycursor.fetchone()
        proId == myresult[0]
        proId += 1
        # proId = proId[:3] + str(int(proId[3])+1)
        # print(proId, "Before")
        name.delete(0, END)
        buy.delete(0, END)
        sell.delete(0, END)

    productsShowBtn = Button(productWin, text="Show Product", command= showProducts,font=("Kanit", 12),fg='gray20',bg='steelblue2',relief="raised",width=15,padx=1).grid(row=3,column=2,columnspan=1)
    productsAddsBtn = Button(productWin, text="Add Products", command= addProducts ,font=("Kanit", 12),fg='gray20',bg='goldenrod1',relief="raised",width=15,padx=1).grid(row=3,column=4,columnspan=1)

    productWin.mainloop()

product()
