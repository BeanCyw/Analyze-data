"""Manage Profit Data"""
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox

from matplotlib.font_manager import FontProperties

import mysql.connector as mysql

global mydb
mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="FWMsod25",
    database="ProductsDatabaseTest"
)


def analyze():
    """Find Top profit"""
    mydb.commit()
    global mycursor
    mycursor = mydb.cursor()

    sql = "SELECT * FROM products "
    mycursor.execute(sql)
    product_db = mycursor.fetchall()
    for data in product_db:
        have_sold = (data[5]-data[6])
        profit = (data[4] * have_sold) - (data[3]*have_sold)
        sql_to_db = "UPDATE products SET profit = '" + str(profit) + \
            "' WHERE productsId = '" + str(data[0]) + "'"
        mycursor.execute(sql_to_db)
        mydb.commit()

    productFromDb = "SELECT * FROM products "
    mycursor.execute(productFromDb)
    productData = mycursor.fetchall()
    if productData == []:
        messagebox.showerror("Error", "ไม่พบข้อมูลกำไร")
    else:
        find_win = Toplevel()
        find_win.title("Top Profit")
        find_win.geometry("600x100+200+100")
        plot_graph = Button(find_win, text='สินค้าที่ทำกำไรมากที่สุด',
                            command=plot,
                            font=("TH Sarabun New", 15+10)).pack()
        product_id = []
        product_name = []
        category = []
        buy_price = []
        sell_price = []
        profit = []
        for data in productData:
            product_id.append(data[0])
            product_name.append(data[1])
            category.append(data[2])
            buy_price.append(data[3])
            sell_price.append(data[4])
            profit.append(data[7])

        global df
        df = pd.DataFrame({
            'Product ID': product_id,
            'Product Name': product_name,
            'Category': category,
            'Buy Price': buy_price,
            'Sell Price': sell_price,
            'Profit': profit
        })

        plt.rcParams["font.family"] = "Th Sarabun New"
        plt.rcParams['font.size'] = 20

        df = df.sort_values(by=['Profit'], ascending=False)
        print(len(df))
        global len_of_data
        len_of_data = df['Profit'].head(5)[df['Profit'] != 0]


def plot():
    """plot pie graph as top 5 max profit"""
    if len(df) < 5:
        label = df['Product Name'].head(len(len_of_data))[df['Profit'] != 0]
        val = df['Profit'].head(len(len_of_data))
        colors = ["lightsteelblue", "lightpink", "bisque", "paleturquoise",
                  "mediumaquamarine"]
        ax = plt.gca()
        ax.set_title(u'%d อันดับ สินค้าที่ทำกำไรมากที่สุด' %
                     (len(len_of_data)))
        ax.pie(val, labels=label, startangle=90, autopct="%1.1f%%",
               colors=colors)
        plt.show()
    else:
        label = df['Product Name'].head(5)[df['Profit'] != 0]
        val = df['Profit'].head(5)[df['Profit'] != 0]
        colors = ["lightsteelblue", "lightpink", "bisque", "paleturquoise",
                  "mediumaquamarine"]
        ax = plt.gca()
        if len(len_of_data) < 5:
            ax.set_title(u'%d อันดับ สินค้าที่ทำกำไรมากที่สุด' %
                         (len(len_of_data)))
        else:
            ax.set_title(u'5 อันดับ สินค้าที่ทำกำไรมากที่สุด')
        ax.pie(val, labels=label, startangle=90, autopct="%1.1f%%",
               colors=colors)
        plt.show()


def do_small():
    """do program small"""
    plt.rcParams["font.family"] = "Th Sarabun New"
    plt.rcParams['font.size'] = 20
    label = ('', '')
    val = (0, 0)
    plt.pie(val, labels=label)
