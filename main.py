import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
client = commands.Bot(command_prefix = '.',  case_insensitive=True, help_command = None, intents = intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


#-------------------------------------------------------------------------------------------------------------------------

#creating a check so only my user can execute the commands in this file
def hackerman(ctx):
    return ctx.author.id == 345234588857270283

#-------------------------------------------------------------------------------------------------------------------------

@client.command()
@commands.check(hackerman)
async def load(ctx, extension): 
    client.load_extension(f'Cogs.{extension}')
    print(f'loaded: {extension}')



#-------------------------------------------------------------------------------------------------------------------------

@client.command()
@commands.check(hackerman)
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    print(f'unloaded: {extension}')

#-------------------------------------------------------------------------------------------------------------------------

@client.command()
@commands.check(hackerman)
async def reload(ctx, extension):
    client.reload_extension(f'Cogs.{extension}')
    print(f'reloaded: {extension}')

#-------------------------------------------------------------------------------------------------------------------------

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        
      try:
          
        client.load_extension(f'Cogs.{filename[:-3]}')
        print(f'loaded: {filename}')
        
      except:
          
          print(f'Couldnt load {filename}')
          
#-------------------------------------------------------------------------------------------------------------------------

client.run(os.getenv('DISCORD_TOKEN_IPL'))
