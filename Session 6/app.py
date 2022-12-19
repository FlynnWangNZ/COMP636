from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/listsuppliers")
def listsuppliers():
    connection = getCursor()
    connection.execute("SELECT * FROM suppliers;")
    supplierList = connection.fetchall()
    print(supplierList)
    return render_template("listsuppliers.html", supplierlist = supplierList)    

@app.route("/productorders")
def productorders():
    connection = getCursor()
    connection.execute("select product_id, product_name, order_id, quantity, unit_price, discount, quantity_per_unit, category from order_details inner join products on order_details.product_id = products.id order by product_id;")
    productOrders = connection.fetchall()
    # print(supplierList)
    return render_template("productorders.html", productorders = productOrders)