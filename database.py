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
def getEncouragements(connection):
    sql = "SELECT expression FROM ENCOURAGEMENTS"
    cheers = []
    with connection:
        data = connection.execute(sql)
        for row in data:
            cheers.append(row[0])
        return cheers


# read stored questions

# insert new question
def insertQuestion(connection, author, name, timestamp, content):
    # ! DEBUG
    print(f'INSERT INTO QUESTIONS /{author}/{name}/{content}/{timestamp}/')
    sql = "INSERT INTO QUESTIONS (QUESTION, AUTHOR, TIMESTAMP, STATUS) VALUES (?, ?, ?, ?)"
    data = (content, author, timestamp, "Not Answered")
    connection.execute(sql, data)
    # get the id automatically generated
    # TODO
    # select with the same data including timestamp
    # return ID

# update question with temptative answer
# pending to accept

# update question with acceptance to answer