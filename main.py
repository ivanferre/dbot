# for the discord bot
import discord

# to use the APIs
import requests

# for the environment
import os
from dotenv import load_dotenv

import json
import random   # encouragement

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

# list of words that trigger bot's actions
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

# we are performing a Stop
ongoingStop = False
ongoingStopUser = ''

# answers to the triggers
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "Don't give up, you still have us."
]

# Commands List
commands_list = [
    "$hello           Greetings.",
    "$inspire         Receive an inspiring quote.",
    "$help            List available commands.",
    "$stopinstance    (implementation in progress)",
    "$confirmstop     (implementation in progress)",
    "$translate       (implementation in progress)",
    "$meeting         (implementation in progress)",
    "$question        (implementation in progress)",
    "$answer          (implementation in progress)"
]

# Get a quote from the Zenquotes API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# Log the bot has logged in.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Listener
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

# TODO: Replace message.author by user's name
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello, {message.author}!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$help'):
        s = "These are the available commands:"
        await message.channel.send("These are the available commands:")
        while s in commands_list:
            await message.channel.send(s)
        else:
            await message.channel.send("Would you like to suggest further functionality?")

    # translation functions
    # msg == message.content
    if msg.startswith('$translate'):
        # remove '$translate ' from msg
        userText = msg.replace("$translate ", "")
        trad = translator.translate(userText,'en')
        await message.channel.send(f'{message.author} says: {trad.text}.')
#        await message.channel.send(trad.text)
        print(trad.text)

    if msg.startswith('$ubersetz '):
        # remove '$translate ' from msg
        userText = msg.replace("$ubersetz ", "")
        trad = translator.translate(userText,'de')
        await message.channel.send(f'{message.author} sagt: {trad.text}.')
        # ! DEBUG
        await message.channel.send(trad.text)
        print(trad.text)


    # encouragement
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('$stopinstance'):
        ongoingStop = True;
        ongoingStopUser = message.author;
        await message.channel.send('Are you sure you want to STOP the instance, {message.author}?')

# TODO implement actual stop the AWS instance.
# ! FIX: why can't find the definition of the ongoing variables?
    if message.content.startswith('$confirmstop'):
        if (ongoingStop & ({message.author} == ongoingStopUser)):
            await message.channel.send('Goodbye, {message.author} and everybody else!')
        else:
            await message.channel.send('{message.author}, you should not make fun with such important matters.')

btoken = os.getenv('TOKEN')
client.run(btoken)
