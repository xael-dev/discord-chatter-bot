import datetime
from discord.ext import commands
from calendar_setup import get_calendar_service


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, context):
        await context.send("pong")

    # Make a rudimentary command to change the VC name, may not be the best way to implement atm.
    @commands.command()
    async def name(self, context, *args):
        print("Voice chat name has changed to" + str(args))
        await context.send(" ".join(args))

    # @commands.command()
    # abstract it out to its own code in the future
    # async def get_calendars(self, ctx):
    #     def main():
    #         service = get_calendar_service()
    #         print('Getting list of calendars')
    #         calendars_result = service.calendarList().list().execute()
    #         calendars = calendars_result.get('items', [])
    #         if not calendars:
    #             print('No calendars found.')
    #             for calendar in calendars:
    #                 summary = calendar['summary']
    #                 id = calendar['id']
    #                 primary = "Primary" if calendar.get('primary') else ""
    #                 print("%s\t%s\t%s" % (summary, id, primary))
    #     # if __name__ == '__main__':
    #     #     main()
    #     await ctx.send("grabbing calendar list")
    # @commands.command()
    # async def get_events(self, ctx):
    #     def main():
    #         service = get_calendar_service()
    #         now = datetime.datetime.utcnow().isoformat() + 'Z'
    #         events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                               maxResults=10, singleEvents=True, orderBy='startTime').execute()
    #         events = events_result.get('items', [])
    #         for event in events:
    #             start = event['start'].get(
    #                 'dateTime', event['start'].get('date'))
    #             print(start, event['summary'])
    #         if events:
    #             print("i got the events")
    #         else:
    #             print("none found")
    #     await ctx.send(events_result)


def setup(bot):
    bot.add_cog(Basic(bot))
