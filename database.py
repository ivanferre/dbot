# read_db.py

# acquire the sqlite library
import sqlite3 as sl

# get the global application variables
from globals import *

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
# AUTOINCREMENT is not recommended when creating KEYs, as explained in
# https://www.sqlitetutorial.net/sqlite-autoincrement/
# RETURNING is not standard SQL, but an extension, as explained in
# https://www.sqlite.org/lang_returning.html
# https://docs.python.org/3/library/sqlite3.html
def insertQuestion(connection, author, name, content, timestamp):
    # ! DEBUG
    print(f'INSERT INTO QUESTIONS /{author}/{name}/{content}/{timestamp}/')

    sql = "INSERT INTO QUESTIONS (QUESTION, AUTHOR, NAME, TIMESTAMP, STATUS, REMINDPERIOD, DEADLINE) VALUES (?, ?, ?, ?, ?, ?) RETURNING id"
    data = (content, author, timestamp, "New", reminderPeriod, answersDeadline)

    # See about Connection Manager in
    # https://docs.python.org/3/library/sqlite3.html
    try:
        with connection:
            id = connection.execute(sql, data)
    except:
        print(f'{sql} failed.')

    print(f'insertQuestion returns {id}')   # ! DEBUG
    return id

    # TODO
    # get the id automatically generated
    # select with the same data including timestamp
    # return ID

# TODO
# update question with temptative answer
# pending to accept
#
# TODO
# update question with acceptance to answer
