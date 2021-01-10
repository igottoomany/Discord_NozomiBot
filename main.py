import discord
from discord.ext import commands
import nozomiSearch

client = commands.Bot(command_prefix='!')



@client.event
async def on_ready():
    print("the bot is online")

@client.command(aliases=['search','hello'])
async def print_hello(ctx,*question):
    await ctx.send(file=discord.File('/Users/leolee/Documents/Project/pythonProject/DownloadFile/sample.jpg'))



@client.command(aliases=['get'])
async def get_post(ctx, *question):
    await ctx.channel.purge(limit=1)
    fileName = nozomiSearch.search(question)

    if(fileName == '' or fileName == None):
        await ctx.send(file=discord.File('/Users/leolee/Documents/Project/pythonProject/images/notEvenHitomi.jpg'))
        return
    else:
        await ctx.send(file=discord.File('/Users/leolee/Documents/Project/pythonProject/DownloadFile/'+fileName))

    nozomiSearch.clear_downloadDir(fileName)



@client.command(aliases=['reset'])
async def reset_channel(ctx, length = 10):
    await ctx.channel.purge(limit=length)

client.run('Nzk3NzU3MjQzMzk0ODgzNTk1.X_rHVA.Ez5QQvPZ_x3MiIoyLg4jAVZv1UY')