import discord

async def logger(client, message):

        channel = client.get_channel(938474079881687170)
        

        embed = discord.Embed(
            title = 'Logs',
            color = discord.Color(0xd900ff)
        )

        embed.add_field(
            name = 'Error',
            value = message
        )

        await channel.send(embed = embed)