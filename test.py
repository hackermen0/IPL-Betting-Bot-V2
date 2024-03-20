import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def test(ctx : discord.ApplicationContext):
    embed = discord.Embed(title = "Ramesh")
    embed.add_field(name = "bolesh", value = "kanesh")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/894851964406468669/1215972470633402538/Banner_0.png?ex=65feb19c&is=65ec3c9c&hm=49ca5a9d1d6ce8742cc43eb36353af5375691db286dc63255dd270e845c29cfa&")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/894851964406468669/1204678788131192862/image-not-found.png?ex=65fa858c&is=65e8108c&hm=62685e494d7256089a0f35966353b564d424aa213d419215e49fe910ad4cb5fb&")

    await ctx.send(embed = embed)

client.run(os.getenv('DISCORD_TOKEN_TEST'))