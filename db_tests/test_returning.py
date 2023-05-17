# /usr/local/python

# ! TODO
# Use RETURNING to get the id of the new row,
# without having to execute a SELECT on the same data.

# acquire the sqlite library
import sqlite3

con = sqlite3.connect("test.db")
print("Connected.")

# con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
# Successful, con.commit() is called automatically afterwards
# with con:
#    con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))

# con.rollback() is called after the with block finishes with an exception,
# the exception is still raised and must be caught

rv = 0
print(f'BEFORE TRY rv = {rv}')

try:
    sql = "INSERT INTO USER(name, age) VALUES(?, ?)"
    with con:
        print("Execute INSERT")
        cursor = con.execute(sql, ("Ramon", 25))
        rv = cursor.lastrowid
        print(f'TRY rv = {rv}')
        con.commit()
except sqlite3.IntegrityError:
    print("Error in INSERT block")
    print(f'EXCEPT rv = {rv}')

print(f'AFTER rv = {rv}')
# Connection object used as context manager only commits or rollbacks transactions,
# so the connection object should be closed manually
con.close()
