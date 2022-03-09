# bot.py
import os
import random

from discord import Intents
from discord import Embed
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


@bot.command(name='sustainable-masks')
@commands.dm_only()
async def sutainable_masks(ctx):

    masks = ['[Vida FDA-Registered KN95 Mask](https://shopvida.com/products/high-protection-recyclable-masks?clickId=3895629537&utm_campaign=88849&utm_medium=affiliate&utm_source=pepperjam). These masks from South Korean manufacturer VIDA come with a prepaid shipping label that you can use to send your masks back for proper recycling!',
             '[Turmerry USA-Made Disposable Face Masks, 50-Pack](https://www.turmerry.com/products/usa-made-50-pcs-disposable-3-ply-filter-mask-earloop-face-masks?irclickid=VAV1oP36vxyIWsjTq9SrI0ZtUkGWfvR6EWIyzM0&irgwc=1). These masks from Turmerry are shipped in packages made of recyclable materials, reducing their enviromental overhead. Turmerry has also committed to plant a tree in the Amazon for every sale they make',
             '[Etiko Organic Fair-Trade Black Face Mask](https://etiko.com.au/products/facemask-organic-fairtrade-black?_pos=1&_sid=3f2a6103b&_ss=r). These masks from Eitko are made with organic cotton, thus limiting the nummber of chemicals and pollutants used in their product',
             '[Repurposed by Karen Upcycled Handmade Face Mask With Nose Wire](https://www.etsy.com/listing/934527215/zero-wasterepurposedupcycled-fabric?source=aw&utm_source=affiliate_window&utm_medium=affiliate&utm_campaign=us_location_buyer&utm_content=173843&awc=6220_1646762883_d4ba342c90642d050ee54393d6333f4b&utm_term=0). These masks from Etsy are made using deadstock fabrics: leftover fabrics from textile mills. These masks are made out of fabrics that might have otherwise been thrown out!']

    masks = ''.join('\n •{}'.format(x) for x in masks)
    response = f'Here\'s a list of various sustainable masks:\n>>> {masks}'

    embed = Embed()
    embed.description = response

    await ctx.send(embed=embed)


@bot.command(name='mask-recycling')
@commands.dm_only()
async def mask_recycling(ctx):

    response = 'Terracycle offers a one of a kind mask recycling program. They offer a product called the Zero Waste Box. Consumers can dispose of their 3-ply surgical, dust masks, KN95, and N95 masks into a Zero Waste Box and then send the boxes back to Terracycle for recycling. These boxes are a great solution for local communities: put up one of these boxes in a centralized area and allow groups of people to dipose of their masks. For more information look [here](https://www.terracycle.com/en-US/pages/ppe-recycling) and [here](https://www.fishersci.com/us/en/scientific-products/publications/lab-reporter/2021/issue-2/reducing-the-environmental-impact-of-face-masks.html).'

    embed = Embed()
    embed.description = response

    await ctx.send(embed=embed)


@bot.command(name='uiuc-mask-program')
@commands.dm_only()
async def uiuc_mask(ctx):

    locations = ['507 East Green Street', 'Ag Engineering Science Building', 'Bevier Hall''Chemical & Life Science Lab', 'Chemistry Annex', 'Enterprise Works', 'Garage and Car Pool', 'Harker Hall', 'Housing Food Stores, Loading Dock Office Room 32',
                 'Illini Union', 'Krannert Center for the Performing Arts', 'Lincoln Hall', 'Mumford Hall', 'National Center for Supercomputing Applications', 'Noyes Lab', 'Roger Adams Lab', 'Transportation Building', 'Turner Hall']

    locations = ''.join('\n •{}'.format(x) for x in locations)

    response = f'UIUC has partnered with Terracycle and setup mask recylcing boxes throughout campus. To request a box for a new location you can contact: recycling@illinois.edu. In the meantime here is a list of locations with Terracycle boxes:\n>>> {locations}'

    await ctx.send(response)


@bot.command(name='mask-enviro-impact')
@commands.dm_only()
async def mask_impact(ctx):

    embed = Embed()
    embed.title = 'The Enviromental Impact of Masks'
    embed.description = 'As a result of the COVID-19 pandemic, face masks have become an essential part of our lives. However, the increased use and disposal of masks are now resulting in environmental impacts that reach well past the pandemic:'

    facts = ['Since the pandemic began, the proportion of masks in our litter has increased by 80-fold: from a measly 0.01%, masks now make up 0.8%% of our litter (1)',
             'Additionally, the inaccessibility of N95 masks at the beginning of the pandemic, led to the wide adoption of cotton face masks. These masks have a 20% CO2 footprint than their N95 counterparts (2)', 'This is especially concerning since in 2020 alone, when cotton masks would have been the most ubiquitous, scientists estimate that 1.6 billion masks ended up in the ocean (3).']
    citations = ['https://www.nature.com/articles/s41893-021-00824-1/', 'https://ecochain.com/knowledge/footprint-face-masks-comparison/',
                 'https://www.newsy.com/stories/face-masks-are-hurting-the-environment/']

    facts = ''.join('\n • {}'.format(x) for x in facts)
    citations = ''.join('\n{} {}'.format(idx + 1, x) for idx, x in enumerate(citations))

    embed.add_field(name='The Facts:', value=f'\n>>> {facts}', inline=True)
    embed.set_footer(text=citations)

    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.PrivateMessageOnly):
        # Do nothing on this error to avoid spamming non-dm channels
        # pass
        print(exception)
        # await ctx.send("DM me this command to use it.")

bot.run(TOKEN)
