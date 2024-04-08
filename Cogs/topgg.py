import sys

path = sys.path[0].replace('\Cogs', '')
sys.path.append(path)

from discord.ext import commands
import discord
from discord import ApplicationContext, slash_command
from Modules.dbFunctions import setBonus
from datetime import datetime
import os
import requests

def hackerman(ctx):
    return ctx.author.id == 345234588857270283

class TopGG(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(name = "claim", description = "Claim your bonus after voting", guild_ids = [506485291914100737])
    async def claim(self, ctx : ApplicationContext):
        
        await ctx.defer()

        token = os.getenv("TOPGG_KEY")

        headers = {
            'Authorization' : token
        }

        link = f"https://top.gg/api/bots/954290531142336542/check?userId={ctx.author.id}"

        r = requests.get(link, headers = headers)

        data = r.json()

        if int(data['voted']) > 0:
            successEmbed = discord.Embed(title = "🎉 YOU HAVE CLAIMED YOUR REWARD 🎉", color = ctx.author.color, timestamp = datetime.now())

            successEmbed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
            successEmbed.set_footer(text = f"Used by {ctx.author.name}")
            
            successEmbed.add_field(name = "\u2800", value = "Thank you for voting for IPL Betting Bot.\nWe have increased your bonus as a reward.")
            successEmbed.set_footer(text = f"Used by {ctx.author.name}")

            setBonus(ctx.author.id, 35)

            await ctx.respond(embed = successEmbed)
        
        else:
            declineEmbed = discord.Embed(title = "It seems like you have not voted", color = ctx.author.color, timestamp = datetime.now())

            declineEmbed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
            declineEmbed.set_footer(text = f"Used by {ctx.author.name}")
            
            declineEmbed.add_field(name = "\u2800", value = "To claim you reward vote at [Top.gg](https://top.gg/bot/954290531142336542).\nAfter voting use the /claim command to receive your reward")
            declineEmbed.set_footer(text = f"Used by {ctx.author.name}")

            await ctx.respond(embed = declineEmbed)

        
def setup(client):
    client.add_cog(TopGG(client))
        
