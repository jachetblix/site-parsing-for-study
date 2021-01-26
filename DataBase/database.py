import sqlite3

conn = sqlite3.connect("../Sql-Data/mydata.db")

sql = "CREATE TABLE books (name TEXT, price TEXT, description TEXT, info TEXT)"
sql = "SELECT * FROM books"
cursor = conn.cursor()

cursor.execute(sql)

res = cursor.fetchall()

for r in res:
    print("Name:", r[0])
    print("Price:", r[1])

conn.close()
