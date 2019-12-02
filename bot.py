# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sorter

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='>')


@bot.command(name='chrom', help='testing with chrom')
async def chrom(ctx):
    print('chrom')
    await ctx.send('https://cdn.discordapp.com/attachments/233316052459585537/645740400560177152/big_chrom.png')

@bot.command(name='fortnite', help='testing with fortnite')
async def roll(ctx, number: int):
    print('fortnite')
    response = 'fortnite ' * number
    await ctx.send(response)

@bot.command(name='text', help='testing with greentext')
async def text(ctx, line):
    response = '```css\n">{}"\n```'
    await ctx.send(response.format(line))

@bot.command(name='info', help='currently supports smash 4 characters and their A moves')
async def text(ctx, char, move):
    response = sorter.sort(char, move)
    await ctx.send(response)


"""
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    thraciaquotes = [
        'thracia 776',
        'fortnite',
        'thracia 776',
        'fortnite',
        'thracia 776',
        'fortnite',
        'thracia 776',
        'fortnite',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike',
        'ike 2',
    ]

    if 'ike' in message.content.lower():
        response = random.choice(thraciaquotes)
        await message.channel.send(response)
"""

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)
