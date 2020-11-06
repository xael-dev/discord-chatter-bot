import discord
from discord.ext import commands

from utils import create_voice_channel, get_category_by_name


class Activities(commands.Cog):

    current_streamers = []

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Activity(name="Type ~help", type=discord.ActivityType.playing)
        await self.bot.change_presence(activity=activity)

    @commands.Cog.listener()  # Listening for user actions on voice channels
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        if not before.channel:
            print(f"{member.name} joined {after.channel.name} channel")

        if before.channel and not after.channel:
            print(f"{member.name} disconnected from channel")

        if before.channel and after.channel:
            if before.channel.id != after.channel.id:
                print(f"{member.name} switched voice channels to {after.channel.name} channel")
            else:
                if member.voice.self_stream:
                    print(f"{member.name} started streaming!")
                    self.current_streamers.append(member.id)
                elif member.voice.self_mute:
                    print(f"{member.name} muted themselves!")

                # Not sure why this doesn't register deafening by the user atm (Not a pressing issue either)
                #  elif member.voice.self_deaf:
                #     print(f"{member.name} deafened themselves!")

                else:
                    for streamer in self.current_streamers:
                        if member.id == streamer:
                            if not member.voice.self_stream:
                                print("User stopped streaming")
                                self.current_streamers.remove(member.id)
                            break

        if after.channel is not None:
            if after.channel.name == "template":
                channel = await create_voice_channel(after.channel.guild, f"{member.name}-conference".lower(), category_name="conference")

                if channel is not None:
                    await member.move_to(channel)

        if before.channel is not None:
            if before.channel.category.id == get_category_by_name(before.channel.guild, "conference").id:
                print(f"{member.name} has left temporary channel")

                if before.channel.name == "template":
                    return

                if len(before.channel.members) == 0:
                    print("The channel is empty")
                    await before.channel.delete()

def setup(bot):
    bot.add_cog(Activities(bot))
