import discord
from discord.ext import commands
import nozomiSearch


description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="!", description=description, intents=intents)


@client.event
async def on_ready():
    print("the bot is online")


@client.command(aliases=["search", "hello"])
async def print_hello(ctx, *question):
    await ctx.send(
        file=discord.File(
            "/Users/leolee/Documents/Project/pythonProject/DownloadFile/sample.jpg"
        )
    )


@client.command(aliases=["get"])
async def get_post(ctx, *question):
    await ctx.channel.purge(limit=1)
    fileName = nozomiSearch.search(question)

    if fileName == "" or fileName == None:
        await ctx.send(
            file=discord.File(
                "/Users/leolee/Documents/Project/pythonProject/images/notEvenHitomi.jpg"
            )
        )
        return
    else:
        await ctx.send(
            file=discord.File(
                "/Users/leolee/Documents/Project/pythonProject/DownloadFile/" + fileName
            )
        )

    nozomiSearch.clear_downloadDir(fileName)
    print("end sending")


@client.command(aliases=["reset"])
async def reset_channel(ctx, length=10):
    await ctx.channel.purge(limit=length)


@client.command()
async def test(ctx):
    await ctx.send("test")


client.run("Nzk3NzU3MjQzMzk0ODgzNTk1.GBtVy_.p-7R6pmxVAsSGjaO9AOcDy8MslCBpLY6JYWs80")
