from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, context):
        await context.send("pong")

    @commands.command() # Make a rudimentary command to change the VC name, may not be the best way to implement atm.
    async def name(self, context, *args):
        print("Voice chat name has changed to" + str(args))
        await context.send(" ".join(args))

def setup(bot):
    bot.add_cog(Basic(bot))
