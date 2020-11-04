from discord.ext import commands

class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, context, *args):
        await context.send(','.join(args))
        pass

def setup(bot):
    bot.add_cog(Testing(bot))
