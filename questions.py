# questions.py

# for the timestamp
# https://www.programiz.com/python-programming/datetime/current-datetime
from read_db import insertQuestion
import discord
from datetime import date
from datetime import datetime
strTimeFormat = '%B %d, %Y at %H:%M:%S'


# database operations

now = datetime.now()
str = '%d/%m/%y %H:%M:%S'
print("now =", now.strftime(strTimeFormat))


def receiveQuestion(msg):
    # TODO
    author = msg.author
    authorName = msg.author.name
    timestamp = now.strftime(strTimeFormat)
    content = msg.replace("$question ", "")

    # record the question in DB: author, author.name, timestamp, content
    idQuestion = insertQuestion(
        msg.author, msg.author.name, content, timestamp)

    # TODO
    # (timetocheck, duetime)
    #
    # thank the author in same channel
    #
    # send the question to the resources channel (include id and say to use it)
    #
    # periodically remind people about the question?
