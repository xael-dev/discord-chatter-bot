from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, context):
        await context.send("pong")

def setup(bot):
    bot.add_cog(Basic(bot))
