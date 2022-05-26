
from tkinter import *
from tkinter import messagebox
import mysql.connector

# Create a database and table if it does not exist

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port="3306"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS password_manager")
mycursor.execute("USE password_manager")
mycursor.execute("CREATE TABLE IF NOT EXISTS accounts (website VARCHAR(255), username VARCHAR(255), password VARCHAR(255))")
if mycursor.fetchone() is None:
    messagebox.showinfo("Success", "Database and table created successfully")
else:
    messagebox.showinfo("Success", "Database and table already exist")
mydb.commit()
mydb.close()




