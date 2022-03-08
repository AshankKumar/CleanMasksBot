# bot.py
import os
import random

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):

    bot_commands = ['!how-to-dispose', '!co2-cloth-mask', '!co2-n95-mask', '!sustainable-masks', '!mask-recycling', '!uiuc-mask-program']
    bot_commands = '\n'.join(bot_commands)

    msg = 'Hi {}, welcome to my Discord server!\nHere are a list of commands I can respond to:\n>>> {}'.format(member.name, bot_commands)

    await member.create_dm()
    await member.dm_channel.send(
        msg
    )


@bot.command(name='99')
@commands.dm_only()
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.PrivateMessageOnly):
        # Do nothing on this error to avoid spamming non-dm channels
        pass
        # await ctx.send("DM me this command to use it.")

bot.run(TOKEN)
