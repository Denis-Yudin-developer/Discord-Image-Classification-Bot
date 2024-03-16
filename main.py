import discord
from discord.ext import commands
import get_model

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def save(ctx):
    # for-each\
    for attachment in ctx.message.attachments:
        filename = attachment.filename
        print(filename)
        await attachment.save(filename)
        await ctx.send("Файл успешно сохранен")
        result = get_model.detect_object(filename)
        await ctx.send(result)

bot.run("MTE1NTE2NzY3NDE5Njg0MDU0OQ.GZl0v-.cSIwTcgeLPPEdn3hRniScqaHiaMhEJEXQJXD_0")