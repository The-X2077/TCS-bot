import discord
import shortjoke
import time
import os
import random
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    print("{0.user} connected without errors".format(client))

logfileid = str(time.time()) + ".txt"
logfile = open(logfileid, "w+", 1)

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    msg_string = username + ":  " + user_message
    #print(f'Message {user_message} by {username} in channel {channel}')
    logfile.write(msg_string)

    if message.author == client.user:
        return
    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == 'hi':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"Bye{username}")
        elif user_message.lower() == "$joke":
            joke = random.choice(shortjoke.jokes)
            await message.channel.send(joke)
            print("[JOKE]", joke)
        elif user_message.lower() == "how are you?":
            await message.channel.send(random.choice(["Good!", "Bad"]))
        elif user_message.lower() == "$screenemote":
            await message.channel.send(
                'https://cdn.discordapp.com/emojis/1021213820028457032.webp?size=96&quality=lossless')


client.run(TOKEN)
