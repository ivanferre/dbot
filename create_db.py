#!/usr/bin/python3
#
# create_database.py - create the dbot database and the necessary tables.
#
# Refs:
# https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
#
# sqlite ubuntu cli client:
# https://manpages.ubuntu.com/manpages/jammy/en/man1/sqlite3.1.html

# acquire the library
import sqlite3 as sl

# create database connection
# if databse does not exist, it's created by python
con = sl.connect('dbot.db')

print("Connected to dbot.db.")

# list of sad words to detect
# with con:
#     con.execute("""
# CREATE TABLE SAD_EXPRESSIONS (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     expression TEXT
# );
# """)

# print ("Creating the sad expressions...")

# populate SAD_EXPRESSIONS
# sql = 'INSERT INTO SAD_EXPRESSIONS (id, expression) values (?, ?)'
# data = [
#     (1, "sad"),
#     (2, "depressed"),
#     (3, "unhappy"),
#     (4, "angry"),
#     (5, "miserable"),
#     (6, "sorrowful"),
#     (7, "dejected"),
#     (8, "regretful"),
#     (9, "downcast"),
#     (10, "downhearted"),
#     (11, "despondent"),
#     (12, "despairing"),
#     (13, "disconsolate"),
#     (14, "out of sorts"),
#     (15, "upset"),
#     (16, "discouraged"),
#     (17, "gloomy")
# ]
# with con:
#     con.executemany(sql, data)
# print("Created SAD_EXPRESSIONS TABLE.")

# print("Creating encouragements...")
# # list of encouragement for sad people
# with con:
#     con.execute("""
# CREATE TABLE ENCOURAGEMENTS (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     expression TEXT
# );
# """)

# # populate ENCOURAGEMENTS
# sql = 'INSERT INTO ENCOURAGEMENTS (id, expression) values (?, ?)'
# data = [
#     (1, "Cheer up!"),
#     (2, "Hang in there."),
#     (3, "You are a great person!"),
#     (4, "Don't give up, you still have us."),
#     (5, "C'mon, you can do it!"),
#     (6, "Get up, stand up!"),
#     (7, "Keep pushing!"),
#     (8, "Keep fighting!"),
#     (9, "Stay strong!"),
#     (10, "Never give up."),
#     (11, "Never say 'die'."),
#     (12, "Always look at the bright side of life"),
#     (13, "Tomorrow will be another day."),
#     (14, "There's always sunshine after rain."),
#     (15, "Give it a try."),
#     (16, "I’m behind you 100%."),
#     (17, "I’ll support you either way."),
#     (18, "Believe in yourself.")
# ]
# with con:
#     con.executemany(sql, data)
# print("Created ENCOURAGEMENTS TABLE.")

# create table QUESTIONS
# @ question - content
# @ author - full discord identifier
# @ timestamp   - date and time of question creation. See strTimeFormat in main.py
# @ status      - "New", "Unaccepted", "Expired", "Closed"
# @ remindPeriod- Minutes between reminders to answer.
# @ deadline    - date and time for question expiration. Same format as timestamp.
print("Creating QUESTIONS...")
with con:
    con.execute("""
CREATE TABLE QUESTIONS (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    author TEXT,
    name TEXT,
    timestamp TEXT,
    status TEXT,
    remindPeriod INTEGER,
    deadline TEXT
);
""")

# create table ANSWERS
# @ question - id of the answered question.
# @ answer      - content of the answer.
# @ author      - full discord identifier
# @ name        - real name of the user.
# @ timestamp   - date and time of answer creation. See strTimeFormat in main.py
# @ status      - "New", "Unaccepted", "Accepted"
print("Creating ANSWERS...")
with con:
    con.execute("""
CREATE TABLE ANSWERS (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    question id,
    answer TEXT,
    author TEXT,
    name TEXT,
    timestamp TEXT,
    status TEXT
);
""")

print("Done")
