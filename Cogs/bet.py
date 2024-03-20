import sys

path = sys.path[0].replace('\Cogs', '')
sys.path.append(path)

import os
from Modules.MatchData import Match
from Modules.dbFunctions import checkUserExists, checkBetExists
import discord
from datetime import datetime
from discord.ui import View
from discord import slash_command
from discord.ext import commands, pages
from views.navigation_buttons import forwardButton, backwardButton, firstButton, lastButton, PageIndicator
from views.bet_buttons import homeTeamButton, awayTeamButton
from views.donation_button import donationButton
from pytz import timezone

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Bet(commands.Cog):
    def __init__(self, client):
        self.client : discord.Bot = client
        self.disabledValue = False
        self.channelID = 894851964406468669
        self.pages = []
        self.embedList = []
        self.buttonList = []
        self.matchBannerList = []
        

    @slash_command(name = 'bet', description = "Lets you bet on the teams that are playing on the current day", guild_ids = [506485291914100737, 912397204306673724])
    @commands.cooldown(
        rate = 1,
        per = 240,
        type = commands.BucketType.user
        ) 
    async def bet(self, ctx):

        self.embedList.clear()
        self.buttonList.clear()


        if checkUserExists(ctx.user.id) == True:


            matchObject = Match()

            matchData = matchObject.getData()

            matchDate = matchData[0]['date']

            channel = await self.client.fetch_channel(self.channelID)

            matchBannerMessage = await channel.history(limit = 1).flatten()

            if matchBannerMessage[0].content != str(matchDate):

                await ctx.respond("Loading...", ephemeral = True)

                for pos, match in enumerate(matchData):

                    matchObject.createBanner(pos, match)

                    matchBanner = discord.File(f"./static/Banners/Banner_{pos}.png", filename=f"Banner_{pos}.png")

                    self.matchBannerList.append(matchBanner)

                matchBannerMessage = await channel.send(content = str(matchDate), files = self.matchBannerList)

                await ctx.edit(content = "Finished Loading!!!")              

                embed = discord.Embed(title = 'IPL Match', description = matchName, timestamp = timeStamp, color = ctx.author.color)
                embed.set_author(name = 'Cricket Bot')
                embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/894851964406468669/962770690442932304/N247P-news-image-6291405812-23776-1597979555.jpg')
                embed.add_field(name = 'Status:', value = matchStatusDisplay, inline = False)
                embed.add_field(name = 'Venue:', value = matchVenue, inline = False)
                embed.add_field(name = 'Date:', value = matchDate, inline = True)
                embed.add_field(name = 'Time:', value = matchTime, inline = True)

            for pos, data in enumerate(matchData):

                matchID = data['id']
                matchName = data['name']
                hasMatchStarted = data['matchStarted']
                matchStatusDisplay = data['status']
                matchVenue = data['venue']
                matchTime = data['dateTimeGMT']
                formattedTIme = datetime.fromisoformat(matchTime).replace(tzinfo = timezone("UTC")).astimezone(tz = timezone("Asia/Kolkata")).strftime("%H:%M (IST)")
                teamsList = data['teams']
            
                timeStamp = datetime.now()

                embed = discord.Embed(title = 'IPL Match', description = matchName, timestamp = timeStamp, color = ctx.author.color)
                embed.set_author(name = 'IPL Betting Bot', icon_url = "https://cdn.discordapp.com/attachments/894851964406468669/1216443254460125266/image.png?ex=66006810&is=65edf310&hm=c20a4dfc1425137f6113630fb08f5afe4b4b2850d83400e997970674f851d517&")
                embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/894851964406468669/962770690442932304/N247P-news-image-6291405812-23776-1597979555.jpg')
                embed.add_field(name = 'Status:', value = matchStatusDisplay, inline = False)
                embed.add_field(name = 'Venue:', value = matchVenue, inline = False)
                embed.add_field(name = 'Date:', value = matchDate, inline = True)
                embed.add_field(name = 'Time:', value = formattedTIme, inline = True)
                embed.set_footer(text = f"Used by {ctx.author.name}")

                if type(matchBannerMessage) == list:
                    embed.set_image(url = matchBannerMessage[0].attachments[pos].url)

                else:
                    embed.set_image(url = matchBannerMessage.attachments[pos].url)
                


                self.embedList.append(embed)

                if checkBetExists(matchID, str(ctx.author.id)) == True or hasMatchStarted == True:  
                    self.disabledValue = True

                else:
                    self.disabledValue = False


                guild = self.client.get_guild(506485291914100737)
                teamEmoji1 = discord.utils.get(guild.emojis, name = str(teamsList[0]).replace(' ', ''))
                teamEmoji2 = discord.utils.get(guild.emojis, name = str(teamsList[1]).replace(' ', ''))


                homeTeamButtonObject = homeTeamButton(label = teamsList[0], disabled = self.disabledValue, matchID = matchID, emoji = teamEmoji1)
                awayTeamButtonObject = awayTeamButton(label = teamsList[1], disabled = self.disabledValue, matchID = matchID, emoji = teamEmoji2)
                donationButtonObject = donationButton()

                self.buttonList.append((homeTeamButtonObject, awayTeamButtonObject))

            
            homeTeamButtonObject, awayTeamButtonObject = self.buttonList[0]

            matchView = View(homeTeamButtonObject, awayTeamButtonObject, donationButtonObject, timeout = 120)
            paginator = pages.Paginator(self.embedList, custom_view = matchView, timeout = 120)

            paginator.embedList = self.embedList
            paginator.buttonList = self.buttonList

            paginator.add_button(forwardButton())
            paginator.add_button(backwardButton())
            paginator.add_button(firstButton())
            paginator.add_button(lastButton())
            paginator.add_button(PageIndicator(label = f"1/{len(self.embedList)}"))

            await paginator.respond(ctx.interaction)

            banners = os.listdir("./Static/Banners")

            if banners != []:
                for file in banners:
                    os.remove(f"./Static/Banners/{file}")
                    print(f"Deleted {file}")

        else:
            await ctx.respond("You don't seem to have a balance\nUse the /balance command to create a balance", ephemeral = True)

        

    @bet.error
    async def bet_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.CommandOnCooldown):
            errorEmbed = discord.Embed(title = "Cooldown", color = ctx.author.color, timestamp = datetime.now())
            errorEmbed.add_field(name = "---------------------------------------------", value=f'Try again in {error.retry_after:.0f}s')
            await ctx.respond(embed = errorEmbed, ephemeral = True)   



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
def setup(client):
    client.add_cog(Bet(client))
        
