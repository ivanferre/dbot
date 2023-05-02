#!/usr/bin/python3
#
# db.py - testing SQLite database features
#
# Source:
# https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
#
# sqlite ubuntu cli client:
# https://manpages.ubuntu.com/manpages/jammy/en/man1/sqlite3.1.html

# acquire the library
print ("Acquire the library...")
import sqlite3 as sl

# create database connection
# if databse does not exist, it's created by python
print ("Connect to database...")
con = sl.connect('test.db')

# create a table
# with con:
#     print ("Create table...")
#     con.execute("""
#         CREATE TABLE USER (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             age INTEGER
#         );
#     """)


# insert multiple entries in one go:
# define the query and the data
sql = 'INSERT INTO  USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]

# execute the sql statement with the data
print("Execute INSERTs...")
#with con:
#    con.executemany(sql, data)

# query the table
with con:
    print("Execute SELECTs")
    data = con.execute("SELECT * FROM USER")
    for row in data:
        print (f'{row[0]} - {row[1]} - {row[2]}')

sql_update = "UPDATE USER SET age = 33 WHERE id = 3"
print(sql_update)
with con:
    data = con.execute(sql_update)
    print(data)

sql_insert = 'INSERT INTO  USER (id, name, age) values(?, ?, ?)'
data = [
    (4, 'Dana', 44),
    (5, 'Eric', 5)
]
print("Execute INSERTs...")
#with con:
    #con.executemany(sql, data)

sql_del = 'DELETE FROM USER WHERE id = 4'
print ("Deleting row 4...")
with con:
    data = con.execute(sql_del)

sql_count = 'SELECT count(*) FROM USER'
print("SQL count...")
with con:
    data = con.execute(sql_count)
    print(data)

print("EOF")
