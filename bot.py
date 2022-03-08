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

bot_commands = ['!how-to-dispose', '!co2-cloth-mask', '!co2-n95-mask', '!sustainable-masks', '!mask-recycling', '!uiuc-mask-program', '!mask-enviro-impact']


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
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


@bot.command(name='how-to-dispose')
@commands.dm_only()
async def carbon_footprint_cloth(ctx):

    source = ''

    practices = ['Don\'t throw masks in the recycling bin. Use the garbage bin.', 'Snip the straps of your mask before throwing them out. Otherwise they can entagle wildlife',
                 'If you have COVID, or have came in contact with someone who has COVID, place your mask in a ziploc bag and write RISK OF CONTAMINATION on the bag before throwing it out', 'Look for mask specific recylcing programs (you can use !mask-recyclin and !uiuc-mask-program to learn more']
    # practices = '\n  •'.join(practices)
    practices = ''.join('\n •{}'.format(x) for x in practices)

    response = f'Single-use masks can be extremely harmful to the enviroment (use !mask-enviro-impact to find out why).\nThis makes it incredibly important to dispose of these masks in the best way possible.\nHere are some best practices for disposing of masks:\n>>> {practices}'

    await ctx.send(response)


@bot.command(name='co2-cloth-mask')
@commands.dm_only()
async def carbon_footprint_cloth(ctx):

    source = 'https://ecochain.com/knowledge/footprint-face-masks-comparison/'
    response = f'The total footprint of one cloth mask is 0.06 kg CO2-equivalent per face mask! The CO2 footprint of the cotton face mask is actually 20% higher than the footprint of the N95 protective face mask.\nSource: {source}'

    await ctx.send(response)


@bot.command(name='co2-n95-mask')
@commands.dm_only()
async def carbon_footprint_ninety_five(ctx):

    source = 'https://ecochain.com/knowledge/footprint-face-masks-comparison/'
    response = f'The total footprint of one N95 mask is 0.05 kg of CO2-equivalent, so around 50 grams. The footprint of one banana is around 80 grams, for comparison.\nSource: {source}'

    await ctx.send(response)


@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.PrivateMessageOnly):
        # Do nothing on this error to avoid spamming non-dm channels
        pass
        # await ctx.send("DM me this command to use it.")

bot.run(TOKEN)
