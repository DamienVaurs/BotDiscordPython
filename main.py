import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check


client = discord.Client()

client = commands.Bot(command_prefix = '!')  here

@client.event
async def on_ready():
    print("bot online") 
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") 

async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) 
    except:
        await ctx.send("bot does not have the kick members permission!")


client.run(os.getenv("TOKEN")) 