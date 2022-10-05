import discord
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

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} in channel {channel}')

    if message.author == client.user:
        return
    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == 'hi':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"Bye{username}")
        elif user_message.lower() == "$joke":
            jokes = [" Can someone please shed more light on how my lamp got stolen?",
                     "im afraid for the calendar.... its days are counted",
                     "what do you call a fish wearing a bowtie? sofishticated.",
                     "Why is she called llene? She stands on equal legs.",
                     "What do you call a gazelle in a lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))
        elif user_message.lower() == "how are you?":
            await message.channel.send(random.choice(["Good!", "Bad"]))
        elif user_message.lower() == "$screenemote":
            await message.channel.send('https://cdn.discordapp.com/emojis/1021213820028457032.webp?size=96&quality=lossless')
client.run(TOKEN)
