import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.',  help_command = None)

TOKEN = 'ODIyMTEyMzU5Mjk5NTQ3MTY2.YFNhzA.HwHPiF1Qf8aBstRIqY-o5qmUNBw'

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(
    type=discord.ActivityType.listening, name=f"{len(client.guilds)} servers | .cmd or .help for help"
    ))
  print('Bot is ready!')
  
@client.command()
async def ping(ctx):
  await ctx.send (f'ping: {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('what command are you even trying to use you little you hot dog')
    
@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('where is the number, add a number you druggo, Add a number like `23`')
    
@client.command()
async def hi(ctx):
  await ctx.send(f'Hello {ctx.author}')
  
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="here are commands", color=0xF30F3)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="`.ping`", value="This command tells you what ms do you have", inline=False)
    embed.add_field(name="`.clear`", value="It delates messages, only works when you have permission to manage message", inline=True)
    embed.add_field(name="`.hi`", value="it will say hi to you", inline=True)
    embed.add_field(name="`.randomnumber` or `.rn`", value="It will generate a random number", inline=True)
    embed.set_thumbnail(url="https://i.picsum.photos/id/1039/6945/4635.jpg?hmac=tdgHDygif2JPCTFMM7KcuOAbwEU11aucKJ8eWcGD9_Q")
    embed.set_footer(text="say: .help2 for page 2")
    
    await ctx.send(embed=embed)

@client.command()
async def cmd(ctx):
    embed=discord.Embed(title="Help", description="here are commands", color=0xF30F3)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="`.ping`", value="This command tells you what ms do you have", inline=False)
    embed.add_field(name="`.clear`", value="It delates messages, only works when you have permission to manage message", inline=True)
    embed.add_field(name="`.hi`", value="it will say hi to you", inline=True)
    embed.add_field(name="`.randomnumber` or `.rn`", value="It will generate a random number", inline=True)
    embed.set_thumbnail(url="https://i.picsum.photos/id/1039/6945/4635.jpg?hmac=tdgHDygif2JPCTFMM7KcuOAbwEU11aucKJ8eWcGD9_Q")
    embed.set_footer(text="say: .help2 for page 2")
    
    await ctx.send(embed=embed)

@client.command()
async def Help(ctx):
    embed=discord.Embed(title="Help", description="here are commands", color=0xF30F3)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="`.ping`", value="This command tells you what ms do you have", inline=False)
    embed.add_field(name="`.clear`", value="It delates messages, only works when you have permission to manage message", inline=True)
    embed.add_field(name="`.hi`", value="it will say hi to you", inline=True)
    embed.add_field(name="`.randomnumber` or `.rn`", value="It will generate a random number", inline=True)
    embed.set_thumbnail(url="https://i.picsum.photos/id/1039/6945/4635.jpg?hmac=tdgHDygif2JPCTFMM7KcuOAbwEU11aucKJ8eWcGD9_Q")
    embed.set_footer(text="say: .help2 for page 2")
    
    await ctx.send(embed=embed)

@client.command()
async def help2(ctx):
    embed=discord.Embed(title="Help", description="here are commands", color=0xF30F3)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="`.kick`", value="This command could kick anyone and you need the permission of administrator", inline=False)
    embed.set_thumbnail(url="https://i.picsum.photos/id/1039/6945/4635.jpg?hmac=tdgHDygif2JPCTFMM7KcuOAbwEU11aucKJ8eWcGD9_Q")
    embed.set_footer(text="say: .help1 to go back to page 1")
    
    await ctx.send(embed=embed)

@client.command()
async def help1(ctx):
    embed=discord.Embed(title="Help", description="here are commands", color=0xF30F3)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="`.ping`", value="This command tells you what ms do you have", inline=False)
    embed.add_field(name="`.clear`", value="It delates messages, only works when you have permission to manage message", inline=True)
    embed.add_field(name="`.hi`", value="it will say hi to you", inline=True)
    embed.add_field(name="`.randomnumber` or `.rn`", value="It will generate a random number", inline=True)
    embed.set_thumbnail(url="https://i.picsum.photos/id/1039/6945/4635.jpg?hmac=tdgHDygif2JPCTFMM7KcuOAbwEU11aucKJ8eWcGD9_Q")
    embed.set_footer(text="say: .help 2 for page 2")
    
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send('a member has been kicked')

@client.command()
async def randomnumber(ctx):
    embed=discord.Embed(title="Random Number Generator", description=(random.randint(1, 101)), color=0x46923)
    await ctx.send(embed=embed)

@client.command()
async def rn(ctx):
    embed=discord.Embed(title="Random Number Generator", description=(random.randint(1, 101)), color=0x46923)
    await ctx.send(embed=embed)




client.run(TOKEN)

