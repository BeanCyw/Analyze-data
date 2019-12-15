"""file to prepare database"""
from tkinter import *
import mysql.connector as mysql


global mydb
mydb = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "FWMsod25",
    database="ProductsDatabaseTest"
)
global mycursor
mycursor = mydb.cursor()

# sql = "ALTER TABLE products ADD profit FLOAT(20)"
# mycursor.execute(sql)
# mydb.commit()

# sql = "ALTER TABLE basket DROP COLUMN productId"
# mycursor.execute(sql)
# mydb.commit()

# sql = "ALTER TABLE products DROP COLUMN productsId"
# mycursor.execute(sql)
# mydb.commit()

# sql = "UPDATE products SET category = 'love', category= 'jubjub'"
# mycursor.execute(sql)
# mydb.commit()

# sql = "UPDATE products SET category = 'dasda', category= '1112'"
# mycursor.execute(sql)
# mydb.commit()

# sql = "DELETE FROM products"
# mycursor.execute(sql)
# mydb.commit()

# sql = "CREATE TABLE basket (productId INT(5) AUTO_INCREMENT PRIMARY KEY, productName VARCHAR(25), category VARCHAR(25), sell FLOAT(25), afterSold INT(25))"
# mycursor.execute(sql)
# print("finish")
# mydb.commit()

# sql = "INSERT INTO products (productsId, productsName, category, buy, sell, beforeSold, afterSold) VALUES (%s, %s, %s,%s ,%s, %s, %s)"
# val = ('0002', 'cxzczx', 'fah', '50.50', '50.50', 0, 0)
# mycursor.execute(sql, val)
# mydb.commit()

# categoryFromDb = "SELECT TOP 1 * FROM products ORDER BY productsId DESC LIMIT 1"
# mycursor.execute(categoryFromDb)
# myresult = mycursor.fetchall()
# category = [cate[2] for cate in myresult]
# print(category, myresult)

# checkId = "SELECT * FROM products WHERE category='love'"
# mycursor.execute(checkId)
# myresult = mycursor.fetchall()
# print(myresult)

# productFromDb = "SELECT * FROM products "
# mycursor.execute(productFromDb)
# productData = mycursor.fetchall()
# for data in productData:
#     print("รหัสสินค้า :%d"%(data[0]))

# sql = "INSERT INTO products (productsId, productsName, category, buy, sell, beforeSold, afterSold) VALUES (%s, %s, %s,%s ,%s, %s, %s)"
# val = ('0002', 'cxzczx', 'fah', '50.50', '50.50', 0, 0)
# mycursor.execute(sql, val)
# mydb.commit()

# productFromDb = "SELECT * FROM products "
# mycursor.execute(productFromDb)
# productData = mycursor.fetchall()
# for data in productData:
#     have_sold = (data[5]-data[6])
#     profit = (data[4] * have_sold) - (data[3]*have_sold)
#     print(data, profit)
#     sql = "UPDATE products SET profit = '" + str(profit) + "' WHERE productsId = '" + str(data[0]) + "'"
#     mycursor.execute(sql)
#     mydb.commit()
