# database.py

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
# See about Connection Manager in
# https://docs.python.org/3/library/sqlite3.html
# @ connection  - must be open, function does not check
# @ author      - discord username
# @ name        - name scrapped from @author
# @ content     - the text of the question
# @ timestamp   - when the question message was detected by the bot
def insertQuestion(connection, author, name, content, timestamp):
    # ! DEBUG
    sqlstr = f'INSERT INTO QUESTIONS (QUESTION, AUTHOR, NAME, TIMESTAMP, STATUS, REMINDPERIOD, DEADLINE) VALUES ({content}, {author}, {name}, {timestamp}, "New", {reminderPeriod}, {answersDeadline})'
    print(sqlstr)

    data = (content, author, name, timestamp,
            "New", reminderPeriod, str(answersDeadline))
    sql = "INSERT INTO QUESTIONS (QUESTION, AUTHOR, NAME, TIMESTAMP, STATUS, REMINDPERIOD, DEADLINE) VALUES (?, ?, ?, ?, ?, ?, ?)"

    newid = 0

    try:
        with connection:
            print("Before connection.execute()")
            cursor = connection.execute(sql, data)
            print("INSERT executed.")
            newid = cursor.lastrowid
            print(f'TRY newid = {newid}')

    except:
        print(f'EXCEPT newid = {newid}')
        newid = -1
        print(f'{sqlstr} failed.')

    print(f'insertQuestion returns {newid}')   # ! DEBUG
    return newid

# TODO
# update question with temptative answer
# pending to accept
#
# TODO
# update question with acceptance to answer


# ! DEBUG
# db = openDatabase('dbot.db')
# id = insertQuestion(db, "Ivan#1638", "Ivan", "Warum?", "17.05.23 15:54:36")
# print("EOF database.py")
