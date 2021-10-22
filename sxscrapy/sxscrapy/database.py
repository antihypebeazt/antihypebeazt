import sqlite3

#sqliteonline.com

conn = sqlite3.connect('myproducts.db')
curr = conn.cursor()

curr.execute("""create table products_tb(
                name text,
                ask integer,
                bid integer
                )""")

curr.execute("""insert into products_tb values ('Python is awesome', 'buildwithpython', 'python')""")

conn.commit()
conn.close()