import random
from discord.utils import get
from discord import Permissions
from discord.ext import commands
from discord import Member

import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 272477035509579786 # Change to your discord id

client = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul " + (message.author.mention))


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    print(ctx)
    await ctx.send(ctx.author)


@bot.command()
async def d6(ctx):
    number = random.randrange(1,7)
    await ctx.send(number)

@bot.command(pass_context=True)
async def admin(ctx, user: discord.Member):
    if get(ctx.guild.roles, name="Admin"):
        await ctx.send("Role already exists")
    else:
        role = await ctx.guild.create_role(name="Admin", permissions=Permissions.all())
        await user.add_roles(role)
        await ctx.send(f"Successfully created and assigned {role.mention}!")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await ctx.guild.ban(user, reason="t'es mort")
    await ctx.send(f"T'es ban looseur")


@bot.command(pass_context=True)
async def count(ctx):
    list = []
    for member in ctx.guild.members:
        status = str(member.status)
        list.append(status +  " - " + member.name)
    list.sort()
    for guy in list:
        await ctx.send(guy)

@bot.command(pass_context=True) #J'ai compris qu'il fallait reposter la question et faire en sorte que le bot rajoute deux réaction, pouce en l'air et pouce vers le bas
async def poll(ctx,arg):
    message = await ctx.send(arg)
    emojiUp = '\N{THUMBS UP SIGN}'
    emojiDown = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emojiUp)
    await message.add_reaction(emojiDown)

@bot.command(pass_context=True)
async def xkcd(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://xkcd.com")
    await ctx.send(embed=embed)


token = "MTAyMjE5Mzg4NDk2MjUwNDgwNA.GBX3vP.DDfUhzHTQyXYFIyRElyrvkMWGzmCdyRh0Hmn8E"
bot.run(token)  # Starts the bot