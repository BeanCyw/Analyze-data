from tkinter import *
from tkinter import messagebox

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

    Label(productWin, text='เพิ่มสินค้า',font=("Kanit", 25),width=10, padx=1,pady=5,fg='goldenrod1',bg='gray20').grid(row=0,column=1,columnspan=5)


    Label(productWin, text='ชื่อสินค้า',font=("Kanit", 16),width=10,fg='azure',bg='gray20',anchor="e").grid(row=1,column=1,columnspan=1)
    name = Entry(productWin, width = 12,font=("Kanit", 12),fg='gray1',bg='gray99')
    name.grid(row=1,column=2)
    
    Label(productWin, text='ประเภทสินค้า',font=("Kanit", 16),width=12,fg='azure',bg='gray20',pady=10,anchor="e").grid(row=1,column=3)
    
    def pro_id_def():
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

    global newCategory
    newCategory = None
    
    clicked = StringVar()
    global categoryOptions
    categoryFromDb = "SELECT * FROM products"
    mycursor.execute(categoryFromDb)
    categoryData = mycursor.fetchall()
    # print(categoryData)
    if categoryData == [] and newCategory == None:
        categoryOptions = ['ไม่พบประเภทสินค้า']
    else:
        categoryOptions = [cate[2] for cate in categoryData]

    clicked = StringVar()

    def updateCategory():
        if newCate.get() == "":
            messagebox.showerror("Error", "กรุณากรอกประเภทสินค้า")
        else:
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
            categoryOptions = ['ไม่พบประเภทสินค้า']
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
        category.configure(width=15, justify=CENTER, font=("Kanit", 10),fg='azure',bg='gray20',borderwidth=0)
        category.grid(row=1,column=4,columnspan=1,sticky='w')

    categoryShow()

    def addCategory():
        global addCate
        addCate = Toplevel()
        addCate.title("AddCategory")
        Label(addCate, text="เพิ่มประเภทสินค้า",font=("Kanit", 13)).pack(side=LEFT)
        global newCate
        newCate = Entry(addCate, width=20,font=("Kanit", 13))
        newCate.pack(side=LEFT)
        submitAddCate = Button(addCate, text='ยืนยัน', command=updateCategory,font=("Kanit", 13)).pack()

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
        if listbox.get(ACTIVE) == "คลิกเลือกประเภทสินค้าที่จะแก้ไข  ":
            messagebox.showerror("Error", "กรุณาระบุสินค้าที่จะแก้ไข")
            edit_show.destroy()
            edit_catagory()

        else:
            global edit_cate
            edit_cate = Toplevel()
            edit_cate.title("Edit_cate")
            global eCate
            Label(edit_cate, text="แก้ไขประเภทสินค้า",font=("Kanit", 13)).pack(side=LEFT)
            eCate = Entry(edit_cate, width=20,font=("Kanit", 13))
            text = (listbox.get(ACTIVE)).lstrip(" ")
            eCate.insert(0, text)
            eCate.pack(side=LEFT)
            submitEditCate = Button(edit_cate, text='ยืนยัน', command=lambda : edit_cate_to_db(text,),font=("Kanit", 13)).pack()

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

    categoryAddBtn = Button(productWin,text="เพิ่ม",command= addCategory ,font=("Kanit", 12),bg='gray20',fg='green2',relief="raised",width=7,padx=1).grid(row=1,column=5,sticky='w')
    categoryEditBtn = Button(productWin,text="แก้ไข",command= edit_catagory ,font=("Kanit", 12),bg='gray20',fg='steelblue1',relief="raised",width=7,padx=1).grid(row=1,column=6,sticky='e')
    
    Label(productWin, text='ราคาซื้อ',font=("Kanit", 16),width=10,fg='azure',bg='gray20',anchor="e").grid(row=2,column=1,columnspan=1)
    buy = Entry(productWin, width = 12,font=("Kanit", 12),fg='gray1',bg='gray99')
    buy.grid(row=2,column=2)
    Label(productWin, text='ราคาขาย',font=("Kanit", 16),width=12,fg='azure',bg='gray20',anchor="e").grid(row=2,column=3,columnspan=1)
    sell = Entry(productWin, width = 15,font=("Kanit", 12),fg='gray1',bg='gray99')
    sell.grid(row=2,column=4,sticky='w')
    

    def edit_pro_to_db(text):
        if "รหัสสินค้า" in text:
            productIdFromDb = "SELECT productsId FROM products "
            mycursor.execute(productIdFromDb)
            productData = mycursor.fetchall()

            for data in productData:
                if int(ePro.get()) == data[0]:
                    messagebox.showerror("Error", "มีรหัสสินค้านี้ในระบบอยู่แล้ว")
                    break
            else:
                text = text[27:]
                sql = "UPDATE products SET productsId = '" + ePro.get() + "'WHERE productsId= '" + text + "'"
                print(sql)
                mycursor.execute(sql)
                mydb.commit()
        elif "ชื่อสินค้า" in text:
            text = text[29:]
            sql = "UPDATE products SET productsName = '" + ePro.get() + "'WHERE productsName= '" + text + "'"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
        elif "ประเภทสินค้า" in text:
            text = text[26:]
            sql = "UPDATE products SET category = '" + ePro.get() + "'WHERE category= '" + text + "'"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
        elif "ราคาซื้อ" in text:
            text = text[28:]
            text = text.rstrip(" บาท")
            sql = "UPDATE products SET buy = '" + ePro.get() + "'WHERE buy= '" + text + "'"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
        elif "ราคาขาย" in text:
            text = text[26:]
            text = text.rstrip(" บาท")
            sql = "UPDATE products SET sell = '" + ePro.get() + "'WHERE sells= '" + text + "'"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()

        productsShowing.destroy()
        edit_pro.destroy()
        showProducts()
        set_cate()


    
    def edit_pro_command():
        global edit_pro
        edit_pro = Toplevel()
        edit_pro.title("Edit Products")
        global ePro
        Label(edit_pro, text="Edit Product",font=("Kanit", 13)).pack(side=LEFT)
        ePro = Entry(edit_pro, width=20,font=("Kanit", 13))
        text = listbox_pro.get(ACTIVE)
        print(text)
        if "สินค้าชิ้นที่  1" in text:
            messagebox.showerror("Error", "กรุณาคลิกเลือกข้อมูลที่ต้องการแก้ไข")
        elif "รหัสสินค้า" in text:
            ePro_id = Entry
            ePro.insert(0, text[27:])
        elif "ชื่อสินค้า" in text:
            ePro.insert(0, text[29:])
        elif "ประเภทสินค้า" in text:
            ePro.insert(0, text[26:])
        elif "ราคาซื้อ" in text:
            text = text.rstrip(" บาท")
            ePro.insert(0, text[28:])
        elif "ราคาขาย" in text:
            text = text.rstrip(" บาท")
            ePro.insert(0, text[26:])
        ePro.pack(side=LEFT)
        submitEditPro = Button(edit_pro, text='Submit', command=lambda : edit_pro_to_db(listbox_pro.get(ACTIVE)),font=("Kanit", 13)).pack()


    def delete_pro_from_db():
        sql = "DELETE FROM products WHERE productsId='" + ePro_delete.get() +"';"
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Info", "ลบสินค้าเรียบร้อย")
        delete_pro.destroy()
        productsShowing.destroy()
        showProducts()
        set_cate()
        pro_id_def()


    def delete_pro_command():
        global delete_pro
        delete_pro = Toplevel()
        delete_pro.title("Edit Products")
        global ePro_delete
        Label(delete_pro, text="ระบุรหัสสินค้า",font=("Kanit", 13)).pack(side=LEFT)
        ePro_delete = Entry(delete_pro, width=20,font=("Kanit", 13))
        text = listbox_pro.get(ACTIVE)
        if "รหัสสินค้า" in text:
            ePro_delete_id = Entry
            ePro_delete.insert(0, text[27:])
        else:
            messagebox.showerror("Error", "กรุณาระบุรหัสสินค้า")
            delete_pro.destroy()
        ePro_delete.pack(side=LEFT)
        submitEditPro = Button(delete_pro, text='ลบสินค้า', command=delete_pro_from_db,font=("Kanit", 13)).pack()


    def showProducts():
        global productsShowing
        productsShowing = Toplevel()
        productsShowing.title("Product Showing")
        categoryFromDb = "SELECT productsName FROM products "
        mycursor.execute(categoryFromDb)
        nameData = mycursor.fetchall()
        global nameShow
        productsShowing.geometry("500x300")
        scrollbar = Scrollbar(productsShowing)
        scrollbar.pack(side=RIGHT, fill=Y)

        global listbox_pro
        listbox_pro = Listbox(productsShowing, yscrollcommand=scrollbar.set,font=("Kanit", 12))
        productFromDb = "SELECT * FROM products "
        mycursor.execute(productFromDb)
        productData = mycursor.fetchall()
        number_of_pro= 0
        for data in productData:
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

        Button(productsShowing,text="แก้ไขสินค้า",command= edit_pro_command ,font=("Kanit", 12),bg='white',fg='gray20',relief="raised",width=20,padx=1).pack()
        Button(productsShowing,text="ลบสินค้า",command= delete_pro_command ,font=("Kanit", 12),bg='white',fg='gray20',relief="raised",width=20,padx=1).pack()


   
        

    checkId = "SELECT * FROM products WHERE productsID=(SELECT MAX(productsId) FROM products)"
    mycursor.execute(checkId)
    myresult = mycursor.fetchone()
    
    pro_id_def()

    def addProducts():
        global proId
        if name.get() == "":
            messagebox.showerror("Error", "กรุณาระบุข้อมูลสินค้า")
        else:
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

    productsShowBtn = Button(productWin, text="แสดงสินค้า", command= showProducts,font=("Kanit", 12),fg='gray20',bg='steelblue2',relief="raised",width=15,padx=1).grid(row=3,column=2,columnspan=1)
    productsAddsBtn = Button(productWin, text="เพิ่มสินค้า", command= addProducts ,font=("Kanit", 12),fg='gray20',bg='goldenrod1',relief="raised",width=15,padx=1).grid(row=3,column=4,columnspan=1)

    productWin.mainloop()

product()
