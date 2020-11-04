# Chatter Bot for Discord
# Written by @alexanderJHarris on github

# Discord imports
import discord
from discord.ext import commands

# Python imports
import config
import pandas


# Initialize the bot object
client = commands.Bot(command_prefix="~")


# As a rule discord requires any events to be run as coroutines (async functions in python)

@client.command(name="version")
async def version(context):  # Context is taking the scope of where this event is called

    myEmbed = discord.Embed( title="Current Version", description="This bot is in version 1.0", color=0x98ff98)
    myEmbed.add_field(name="Version Code: ", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="November 1st, 2020", inline=False)
    myEmbed.set_footer(text="Release version message")
    myEmbed.set_author(name=config.author_name)

    await context.message.channel.send(embed=myEmbed) #using the context param above to send the embed to requested channel

@client.event
async def on_message(message):

    if message == 'send a dm':
        await message.author.send("This is a test DM, have a good day")



# Run the client

client.run(config.bot_token)
