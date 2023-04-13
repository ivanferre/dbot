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

# answers to the triggers
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

btoken = os.getenv('TOKEN')
client.run(btoken)
