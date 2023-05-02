# read_db.py

# acquire the library
import sqlite3 as sl

# create database connection
# if databse does not exist, it's created by python
# @ database filename
# @ returns a connection to a database
# TODO check for errors (file not found, etc.)
def openDatabase(dbfile):
    con = sl.connect(dbfile)
    return con

# read table SAD_EXPRESSIONS and
# populate list sad_words
# @ connection: open database connection
# @ exprlist: list to append the expressions read from database
def getSadExpressions(connection):
    sql = "SELECT expression FROM SAD_EXPRESSIONS"
    exprlist = []
    with connection:
        data = connection.execute(sql)
        for row in data:
            exprlist.append(row[0])
        return exprlist


# read table ENCOURAGEMENTS and
# populate table starter_encouragements

# read stored questions

# insert new question

# update question with temptative answer
# pending to accept

# update question with acceptance to answer

