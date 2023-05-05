#!/usr/bin/python3

# FirstBot discord bot

# importing modules
# -----------------

# for the discord bot
import discord

# for google translator
from googletrans import Translator
import googletrans

# to use the APIs
import requests

# for the environment
import os
from dotenv import load_dotenv

import json
import random   # encouragement

# import database functions
from database import *

# date and time functions
from datetime import date
from datetime import datetime

# globals declaration
# -------------------

# Commands List
commands_list = (
    "$answer          (implementation in progress)",
    "$confirmstop     (implementation in progress)",
    "$hello           Greetings.",
    "$help            List available commands.",
    "$inspire         Receive an inspiring quote.",
    "$meeting         (implementation in progress)",
    "$question        (implementation in progress)",
    "$stopinstance    Requests to stop the AWS EC2 instance.",
    "$translate       Translate text to English",
    "$ubersetz        Translate text to German"
)


# we are not yet performing a Stop
ongoingStop = False
ongoingStopUser = ''

# time format
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
strTimeFormat = '%d.%m.%y %H:%M:%S'

# default minutes between reminders to answer questions
# 60 x 24  = 1440
reminderPeriod = 1440

# default minutes


# Initialization

# open database connection
db = openDatabase('dbot.db')
# list of words that trigger bot's actions
sad_words = getSadExpressions(db)

# answers to the triggers
starter_encouragements = getEncouragements(db)

# Create the Discord bot.
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
load_dotenv()
TOKEN = os.getenv("TOKEN")

# for the translation functionality
translator = Translator(service_urls=[
    'translate.google.com',
])
translator = Translator()

# functions

# Get a quote from the Zenquotes API


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

#############
# Here we go!
#############

# Log the bot has logged in.


@client.event
async def on_ready():
    print('FirstBot logged in as {0.user}'.format(client))

# Listener


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello, {message.author.name}!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$help'):
        await message.channel.send("These are the available commands:")
        for s in commands_list:
            await message.channel.send(s)
        else:
            await message.channel.send("Would you like to suggest further functionality?")

    # translation functions (msg == message.content)
    if msg.startswith('$translate'):
        # remove '$translate ' from msg
        userText = msg.replace("$translate ", "")
        trad = translator.translate(userText, 'en')
        await message.channel.send(f'{message.author} says: {trad.text}')

    if msg.startswith('$ubersetz '):
        # remove '$translate ' from msg
        userText = msg.replace("$ubersetz ", "")
        trad = translator.translate(userText, 'de')
        await message.channel.send(f'{message.author} sagt: {trad.text}')

        # TODO
    if msg.startswith('$question'):
        now = datetime.now()
        content = msg.replace("$question ", "")
        idQuestion = insertQuestion(
            message.author, message.author.name, content, now.strftime(strTimeFormat))
        # thank the author in same channel
        await message.channel.send(f'Dear {message.author.name}, thank you for your very interesting question: {content}')
        # TODO
        # send the question to the resources channel (include id and say to use it)
        # TODO
        # periodically remind people about the question
        # (remindPeriod, deadline)

    if msg.startswith('$answer'):
        # !DEBUG
        userText = msg.replace("$answer ", "")
        await message.channel.send(f'{message.author} answers: {userText}')
        # TODO
        # record the answer...
        #
        # thank the person who answers
        #
        # notify the person who made the question, and ask if it accepts.

    if msg.startswith('$accept'):
        # !DEBUG
        await message.channel.send(f'{message.author} has accepted the answer to her question.')
        # TODO
        # if accept no
        #   notify both
        # else
        #   thank answerer in public (resources channel?)
        # update answer as accepted in db
        # update question as closed in db

    # encouragement
    if any(word in msg for word in sad_words):
        # TODO Make it case-insensitive
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('$stopinstance'):
        global ongoingStop
        global ongoingStopUser
        ongoingStop = True
        ongoingStopUser = message.author
        await message.channel.send(f'Are you sure you want to STOP the instance, {message.author}?')

    if message.content.startswith('$confirmstop'):

        if (ongoingStop & (message.author == ongoingStopUser)):
            # TODO implement actual stop the AWS instance.
            await message.channel.send(f'Goodbye, {message.author.name} and everybody else!')
        else:
            await message.channel.send(f'{message.author.name}, you should not make fun with such important matters.')

btoken = os.getenv('TOKEN')
client.run(btoken)
