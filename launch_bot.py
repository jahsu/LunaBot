# import discord
from discord.ext import commands as cmd
from configuration import config
import commands

bot = cmd.Bot(command_prefix='!')

# we do not want the bot to reply to itself
#     if message.author == client.user:
#        return


@bot.command(pass_context=True)
async def hello(ctx):
    msg = 'Yo whaddup {0.author.mention}'.format(ctx.message)
    await bot.say(msg)

    # if message.content.startswith('!help'):
    #     await client.send_message(message.channel, send_help(message))


@bot.command()
async def welcome():
    await bot.say(commands.welcome.send_welcome())


@bot.command()
async def feature():
    await bot.say(commands.feature.show_features())


@bot.command()
async def wink():
    await bot.say(commands.wink.wink_iu())


@bot.command()
async def peekaboo():
    await bot.say(commands.peekaboo.peek_iu())


@bot.command(pass_context=True)
async def wiki(ctx, *args):
    await bot.say(commands.wiki.query_wiki(ctx, args))


@bot.command()
async def twentyfive():
    await bot.say('https://www.youtube.com/watch?v=d9IxdwEFk1c')


@bot.command()
async def twentythree():
    await bot.say('https://www.youtube.com/watch?v=42Gtm4-Ax2U')


@bot.command()
async def gaming():
    await bot.say('https://media1.tenor.com/images/c8827d28f2821f0c78406565f334a6d0/tenor.gif?itemid=9266360')


@bot.command()
async def k():
    await bot.say('http://i.imgur.com/yyyg94n.gif')


@bot.command()
async def plumpbois():
    await bot.say('P L U M P B O I S  https://media.giphy.com/media/O5GKT0UDGyQLu/giphy.gif')


@bot.command(pass_context=True)
async def say(ctx, *args):
    msg = ' '.join(args).format(ctx.message)
    await bot.say(msg)


@bot.command(pass_context=True)
async def yut(ctx):
    msg = '{0.author.mention} yutted!'.format(ctx.message)
    await bot.say(msg)

# Catch non-existing commands

# @client.event
# async def on_ready():
 #    print('Logged in as')
 #    print(client.user.name)
 #    print(client.user.id)
  #   print('------')

if __name__ == "__main__":
    print("Bot on")
    bot.run(config.Config().bot_token)
#client.run(config.Config().bot_token)
