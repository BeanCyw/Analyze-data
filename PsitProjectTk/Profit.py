{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    15.0\n",
       "3    10.0\n",
       "0     0.0\n",
       "1     0.0\n",
       "Name: Profit, dtype: float64"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from tkinter import *\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.font_manager import FontProperties\n",
    "## Connecting to the database\n",
    "\n",
    "## importing 'mysql.connector' as mysql for convenient\n",
    "import mysql.connector as mysql\n",
    "\n",
    "## connecting to the database using 'connect()' method\n",
    "## it takes 3 required parameters 'host', 'user', 'passwd'\n",
    "global mydb\n",
    "mydb = mysql.connect(\n",
    "    host = \"localhost\",\n",
    "    user = \"root\",\n",
    "    passwd = \"FWMsod25\",\n",
    "    database=\"ProductsDatabaseTest\"\n",
    ")\n",
    "global mycursor\n",
    "mycursor = mydb.cursor()\n",
    "\n",
    "productFromDb = \"SELECT * FROM products \"\n",
    "mycursor.execute(productFromDb)\n",
    "productData = mycursor.fetchall()\n",
    "\n",
    "product_id = []\n",
    "product_name = []\n",
    "category = []\n",
    "buy_price = []\n",
    "sell_price = []\n",
    "profit = []\n",
    "for data in productData:\n",
    "    product_id.append(data[0])\n",
    "    product_name.append(data[1])\n",
    "    category.append(data[2])\n",
    "    buy_price.append(data[3])\n",
    "    sell_price.append(data[4])\n",
    "    profit.append(data[7])\n",
    "\n",
    "df = pd.DataFrame({ \n",
    "'Product ID':product_id,\n",
    "'Product Name':product_name,\n",
    "'Category': category,\n",
    "'Buy Price':buy_price,\n",
    "'Sell Price':sell_price,\n",
    "'Profit':profit\n",
    "})\n",
    "\n",
    "fp = FontProperties(family='Tahoma',size=13)\n",
    "plt.rcParams[\"font.family\"] = \"Kanit\"\n",
    "plt.rcParams['font.size'] = 15\n",
    "    \n",
    "df = df.sort_values(by=['Profit'], ascending=False)\n",
    "a = df['Profit'].head(5)[df['Profit']!=0]\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "'explode' must be of length 'x'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m-------------------------------------------------------------\
          --------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                               \
           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-170-16990aef4402>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[0manalyze\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-170-16990aef4402>\u001b[0m in \u001b[0;36mplot\u001b[1;34m()\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mcolors\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;34m\"lightsteelblue\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"lightpink\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"bisque\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"paleturquoise\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"mediumaquamarine\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0max\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgca\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m     \u001b[0max\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpie\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mval\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabels\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlabel\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstartangle\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m90\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mautopct\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"%1.1f%%\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexplode\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m0.15\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcolors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcolors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m     \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mE:\\Anaconda\\lib\\site-packages\\matplotlib\\__init__.py\u001b[0m in \u001b[0;36minner\u001b[1;34m(ax, data, *args, **kwargs)\u001b[0m\n\u001b[0;32m   1599\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0minner\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1600\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mdata\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1601\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0mmap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msanitize_sequence\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1602\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1603\u001b[0m         \u001b[0mbound\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnew_sig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0max\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mE:\\Anaconda\\lib\\site-packages\\matplotlib\\axes\\_axes.py\u001b[0m in \u001b[0;36mpie\u001b[1;34m(self, x, explode, labels, colors, autopct, pctdistance, shadow, labeldistance, startangle, radius, counterclock, wedgeprops, textprops, center, frame, rotatelabels)\u001b[0m\n\u001b[0;32m   2983\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"'label' must be of length 'x'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2984\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mexplode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2985\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"'explode' must be of length 'x'\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2986\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mcolors\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2987\u001b[0m             \u001b[0mget_next_color\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_patches_for_fill\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_next_color\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: 'explode' must be of length 'x'"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def plot():\n",
    "    \"\"\"plot pie graph as top 5 max profit\"\"\"\n",
    "    label = df['Product Name'].head(5)\n",
    "    val = df['Profit'].head(5)\n",
    "    colors = [\"lightsteelblue\", \"lightpink\", \"bisque\", \
        \"paleturquoise\", \"mediumaquamarine\"]\n",
    "    ax = plt.gca()\n",
    "    ax.pie(val, labels=label, startangle=90, autopct = \"%1.1f%%\", \
        explode = (0.15, 0, 0, 0, 0), colors=colors)\n",
    "    plt.show()\n",
    "\n",
    "analyze()\n",
    "plot()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
