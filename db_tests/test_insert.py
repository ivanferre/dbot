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

print("Let's try!")
try:
    sql = "INSERT INTO lang(name) VALUES(?)"
    with con:
        print("Execute INSERT")
        con.execute(sql, ("Pascal",))
        print("Set the Cursor")
        cur = con.cursor()
        print("Execute SELECT")
        rv = cur.execute("SELECT id FROM lang WHERE name = 'Pascal'")
except sqlite3.IntegrityError:
    print("Error in INSERT block")
    rv = -1

print(f'id = {rv}')
res = rv.fetchone()
print(f'res = {res}')
newid = res[0]
print(f'newid = {newid}')
# Connection object used as context manager only commits or rollbacks transactions,
# so the connection object should be closed manually
con.close()
