import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

import tweepy

my_secret1 = os.environ['TwitterToken']
auth = tweepy.OAuth2BearerHandler(my_secret1)
api = tweepy.API(auth)


username='LMPositif'
tweets_list= api.user_timeline(username, count=1, tweet_mode='extended')
tweet= tweet_list[0]
print(tweet.full_text)

client = discord.Client()

client = commands.Bot(command_prefix = '!') 

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