#!/usr/bin/python3

# FirstBot discord bot

##### importing modules

# for the discord bot
import discord

# to use the APIs
import requests

# for the environment
import os
from dotenv import load_dotenv

import json
import random   # encouragement

# import database functions
from read_db import *

# open database connection
db = openDatabase('dbot.db')

# print("Connected to database.") # ! debug

##### globals declaration

# list of words that trigger bot's actions
sad_words = getSadExpressions(db)
# print (f'We have {len(sad_words)} sad words.')
# print (sad_words)
## old_sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

# answers to the triggers
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "Don't give up, you still have us."
]

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

# we are performing a Stop
ongoingStop = False
ongoingStopUser = ''

##### Initialization

# for the translation functionality
import googletrans
from googletrans import Translator
translator = Translator(service_urls=[
 	'translate.google.com',
])
translator = Translator()

# Create the Discord bot.
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
load_dotenv()
TOKEN = os.getenv("TOKEN")

##### functions

# Get a quote from the Zenquotes API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#####
##### Here we go!
#####

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
            print (s)
            await message.channel.send(s)
        else:
            await message.channel.send("Would you like to suggest further functionality?")

    # translation functions (msg == message.content)
    if msg.startswith('$translate'):
        # remove '$translate ' from msg
        userText = msg.replace("$translate ", "")
        trad = translator.translate(userText,'en')
        await message.channel.send(f'{message.author} says: {trad.text}.')

    if msg.startswith('$ubersetz '):
        # remove '$translate ' from msg
        userText = msg.replace("$ubersetz ", "")
        trad = translator.translate(userText,'de')
        await message.channel.send(f'{message.author} sagt: {trad.text}.')


    # encouragement
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('$stopinstance'):
        global ongoingStop
        global ongoingStopUser
        ongoingStop = True;
        ongoingStopUser = message.author;
        await message.channel.send(f'Are you sure you want to STOP the instance, {message.author}?')

    if message.content.startswith('$confirmstop'):

        if (ongoingStop & (message.author == ongoingStopUser)):
# TODO implement actual stop the AWS instance.
            await message.channel.send(f'Goodbye, {message.author.name} and everybody else!')
        else:
            await message.channel.send(f'{message.author.name}, you should not make fun with such important matters.')

btoken = os.getenv('TOKEN')
client.run(btoken)
