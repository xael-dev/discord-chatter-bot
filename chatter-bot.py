# Chatter Bot for Discord
import discord
import config


# Initialize the bot here
client = discord.Client()


# As a rule discord require these events to be run as coroutines
@client.event
async def on_ready():
    general_channel = client.get_channel(679832307066208440)
    await general_channel.send('Hello Juniors!')


@client.event
async def on_disconnect():
    cromulon_channel = client.get_channel(707682506291412993)
    await cromulon_channel.send("Goodbye!")


@client.event
async def on_message(message):

    if message.content == 'chatter what is your version':
        cromulon_channel = client.get_channel(707682506291412993)
        await cromulon_channel.send("The version is 1.0!")

# Run the client on the server
client.run("NzcxODYxODk3Nzg4MTI5Mjgx.X5ySaA.jLrUMauYqNPo9eHSYGkOUGOtcoo")
