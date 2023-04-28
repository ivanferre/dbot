import discord
import requests

import os
from dotenv import load_dotenv

import json
import random


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
  "You are a great person!"
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

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('$stopinstance'):
        ongoingStop = True;
        ongoingStopUser = message.author;
        await message.channel.send('Are you sure you want to STOP the instance, {message.author}?')

# TODO implement actual stop the AWS instance.
    if message.content.startswith('$confirmstop'):
        if (ongoingStop & ({message.author} == ongoingStopUser)):
            await message.channel.send('Goodbye, {message.author} and everybody else!')
        else:
            await message.channel.send('{message.author}, you should not make fun with such important matters.')

btoken = os.getenv('TOKEN')
client.run(btoken)
