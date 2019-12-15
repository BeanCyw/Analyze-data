"""Main Program"""
from tkinter import *
from tkinter import messagebox
import AddProductsButton as apb
import Stock as stk
import Selling as sll
import Findprofit as fpf
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


def main_program():
    """main windows of program"""
    global main
    main = Tk()
    main.title("Grocery Store")
    main.geometry("400x400+100+100")
    sell_button = Button(main, text='การขาย', command=lambda:
                         sll.selling(), font=("TH Sarabun New", 15+10),
                         width=15).pack(fill=BOTH, expand=TRUE)
    add_pro_button = Button(main, text='คลังสินค้า', command=lambda:
                            apb.product(), font=("TH Sarabun New", 15+10),
                            width=15).pack(fill=BOTH, expand=TRUE)
    stock_button = Button(main, text='สต็อกสินค้า', command=lambda:
                          stk.stock(), font=("TH Sarabun New", 15+10),
                          width=15).pack(fill=BOTH, expand=TRUE)
    ana_button = Button(main, text='สินค้าทำกำไร', command=lambda:
                        fpf.analyze(), font=("TH Sarabun New", 15+10),
                        width=15).pack(fill=BOTH, expand=TRUE)

    main.mainloop()


def destroy_main_pro():
    """destroy main windows"""
    main.destroy()


fpf.do_small()
main_program()
