import sys

path = sys.path[0].replace('\Cogs', '')
sys.path.append(path)

from discord.ext import commands
import discord
from discord import ApplicationContext, slash_command
from datetime import datetime

class Utility(commands.Cog):

    def __init__(self, client):

        self.client = client


    @slash_command(name = "ping", description = "Returns the latency of the bot", guild_ids = [506485291914100737])
    async def ping(self, ctx : ApplicationContext):

        embed = discord.Embed(title = "Ping", color = ctx.author.color, timestamp = datetime.now())

        embed.add_field(name = "Latency:", value = f"{round(self.client.latency * 1000)}ms")


<<<<<<< HEAD
        embed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
=======
        embed.set_author(name = 'FIFA Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1043592586151071925/botpfp.png")
>>>>>>> caed42f88b689c05a1fd55f92681f52329d71a4f
        embed.set_footer(text = f"Used by {ctx.author.name}")

        await ctx.respond(embed = embed)


    @slash_command(name = "help", description = "Shows the help command", guild_ids = [506485291914100737])
    async def help(self, ctx : ApplicationContext):

        embed = discord.Embed(title = "Help", color = ctx.author.color, timestamp= datetime.now())

<<<<<<< HEAD
        embed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
        embed.set_footer(text = f"Used by {ctx.author.name}")

        embed.add_field(name = "</balance:1215973218955956317>:", value = "Lets you check the amount of money you have to bet", inline = False)
        embed.add_field(name = "</bet:1216062332518531223>:", value = "Lets you bet on the teams that are playing on the current day", inline = False)
        embed.add_field(name = "</leaderboard:1215973218955956319>:", value = "Shows the leaderboard with the top betters", inline = False)
        embed.add_field(name = "</how:1215714112093425705>:", value = "Shows you how to use this bot", inline = False)
        embed.add_field(name = "</donate:1215714112093425706>:", value = "If you like this bot you can use this command to donate", inline = False)
        embed.add_field(name = "</ping:1215703916365484105>:", value = "Returns the latency of the bot", inline = False)
        embed.add_field(name = "</stats:1215973218955956320>:", value = "Shows the amount of money betted on the current day matches", inline = False)
=======
        embed.set_author(name = 'FIFA Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1043592586151071925/botpfp.png")
        embed.set_footer(text = f"Used by {ctx.author.name}")

        embed.add_field(name = "</balance:1043846403165782066>:", value = "Lets you check the amount of money you have to bet", inline = False)
        embed.add_field(name = "</bet:1043846403165782073>:", value = "Lets you bet on the teams that are playing on the current day", inline = False)
        embed.add_field(name = "</leaderboard:1043846403165782068>:", value = "Shows the leaderboard with the top betters", inline = False)
        embed.add_field(name = "</how:1215714112093425705>:", value = "Shows you how to use this bot", inline = False)
        embed.add_field(name = "</donate:1043887595882561660>:", value = "If you like this bot you can use this command to donate", inline = False)
        embed.add_field(name = "</ping:1043887595882561657>:", value = "Returns the latency of the bot", inline = False)
        embed.add_field(name = "</stats:1045021111492030475>:", value = "Shows the amount of money betted on the current day matches", inline = False)
>>>>>>> caed42f88b689c05a1fd55f92681f52329d71a4f

        await ctx.respond(embed = embed)


    @slash_command(name = "how", description = "Shows you how to use this bot", guild_ids = [506485291914100737])
    async def how(self, ctx : ApplicationContext):

        embed = discord.Embed(title = "How", color = ctx.author.color, timestamp= datetime.now())

<<<<<<< HEAD
        embed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
        embed.set_footer(text = f"Used by {ctx.author.name}")

        embed.add_field(name = "How to play:", value = """
        Use the </balance:1215973218955956317> command to create and check the amount of money you have to bet.

        After that use the </bet:1216062332518531223> command to bet on the teams playing on that current day, you can use the navigation buttons to bet on multiple matches.
        If the team you betted on wins, you will be awarded a percentage of total amount betted on that match the next day.

        Use the </leaderboard:1215973218955956319> command to see the top betters.    
=======
        embed.set_author(name = 'FIFA Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1043592586151071925/botpfp.png")
        embed.set_footer(text = f"Used by {ctx.author.name}")

        embed.add_field(name = "How to play:", value = """
        Use the </balance:1043846403165782066> command to create and check the amount of money you have to bet.

        After that use the </bet:1043846403165782073> command to bet on the teams playing on that current day, you can use the navigation buttons to bet on multiple matches.
        If the team you betted on wins, you will be awarded a percentage of total amount betted on that match the next day.

        Use the </leaderboard:1043846403165782068> command to see the top betters.    
>>>>>>> caed42f88b689c05a1fd55f92681f52329d71a4f
        """)

        await ctx.respond(embed = embed)

    @slash_command(name = "donate", description = "If you like this bot you can use this command to donate", guild_ids = [506485291914100737])
    async def donate(self, ctx : ApplicationContext):
        embed = discord.Embed(title = "Donate", color = ctx.author.color, timestamp= datetime.now())

<<<<<<< HEAD
        embed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
=======
        embed.set_author(name = 'FIFA Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1043592586151071925/botpfp.png")
>>>>>>> caed42f88b689c05a1fd55f92681f52329d71a4f
        embed.set_footer(text = f"Used by {ctx.author.name}")


        embed.add_field(name = "\u2800", value = """
        If you liked this bot, please consider donating

        It will help with the smoother functioning of this bot and will also help with the further development of it

        All donations are appreciated ♥️

        [Donate Here](https://paypal.me/FIFABettingBot)

        """
        )

        await ctx.respond(embed = embed)

<<<<<<< HEAD
=======

>>>>>>> caed42f88b689c05a1fd55f92681f52329d71a4f
def setup(client):
    client.add_cog(Utility(client))
