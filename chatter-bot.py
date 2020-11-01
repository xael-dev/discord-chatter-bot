# Chatter Bot for Discord
# Written by @alexanderJHarris on github
import discord
import config


# Initialize the bot here
client = discord.Client()


# As a rule discord requires any events to be run as coroutines (async functions in python)

# @client.event
# async def on_ready():
#     general_channel = client.get_channel(679832307066208440)
#     await general_channel.send('Hello Juniors!')


@client.event
async def on_disconnect():
    cromulon_channel = client.get_channel(707682506291412993)
    await cromulon_channel.send("Goodbye!")


@client.event
async def on_message(message):

    if message.content == 'chatter what is your version':
        cromulon_channel = client.get_channel(707682506291412993)

        myEmbed = discord.Embed(title="Current Version", description="This bot is in version 1.0", color=0x98ff98)
        myEmbed.add_field(name="Version Code: ", value="v1.0.0",inline=False)
        myEmbed.add_field(name="Date Released:", value="November 1st, 2020", inline=False)
        myEmbed.set_footer(text="Release version message")
        myEmbed.set_author(name="Alexander Harris")


        await cromulon_channel.send(embed=myEmbed)

# Run the client on the server
client.run(config.bot_token)
