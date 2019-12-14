from tkinter import *
from tkinter import messagebox
import AddProductsButton as apb
import Stock as stk
import Selling as sll
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


def main_program():
    """main windows of program"""
    main = Tk()
    main.title("Grocery Store")
    main.geometry("300x300+100+100")
    sell_button = Button(main, text='การขาย', command=lambda : sll.selling(),font=("TH Sarabun New", 15), width=15).pack(fill= BOTH, expand= TRUE)
    add_pro_button = Button(main, text='คลังสินค้า', command=lambda : apb.product(),font=("TH Sarabun New", 15), width=15).pack(fill= BOTH, expand= TRUE)
    stock_button = Button(main, text='สต็อกสินค้า', command=lambda : stk.stock(),font=("TH Sarabun New", 15), width=15).pack(fill= BOTH, expand= TRUE)
    ana_button = Button(main, text='วิเคราะห์การขาย', command=lambda : apb.product(),font=("TH Sarabun New", 15), width=15).pack(fill= BOTH, expand= TRUE)

    main.mainloop()

main_program()