import discord
from discord.ext import commands as cmd
from configuration import config
import commands

bot = cmd.Bot(command_prefix='!')
bot.add_cog(commands.music.VoiceState(bot))
bot.add_cog(commands.music.Music(bot))

# we do not want the bot to reply to itself
#     if message.author == client.user:
#        return


class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = '*{0.title}* uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)


def check_opus():
    if not discord.opus.is_loaded():
        discord.opus.load_opus('opus')


@bot.command(pass_context=True, no_pm=True)
async def hello(ctx):
    msg = 'Yo whaddup {0.author.mention}'.format(ctx.message)
    await bot.say(msg)

    # if message.content.startswith('!help'):
    #     await client.send_message(message.channel, send_help(message))


@bot.command(no_pm=True)
async def welcome():
    await bot.say(commands.welcome.send_welcome())


@bot.command(no_pm=True)
async def feature():
    await bot.say(commands.feature.show_features())


@bot.command(no_pm=True)
async def wink():
    await bot.say(commands.wink.wink_iu())


@bot.command(no_pm=True)
async def peekaboo():
    await bot.say(commands.peekaboo.peek_iu())


@bot.command(pass_context=True)
async def wiki(ctx, *args):
    await bot.say(commands.wiki.query_wiki(ctx, args))


@bot.command(pass_context=True, no_pm=True)
async def twentyfive(ctx):
    url = 'https://www.youtube.com/watch?v=d9IxdwEFk1c'
    bot_music = bot.get_cog('Music')
    player = await commands.music.Music.play_music(bot_music, ctx, url)
    await commands.music.Music.enque(bot_music, ctx, VoiceEntry(ctx.message, player))


@bot.command(no_pm=True)
async def twentythree():
    await bot.say('https://www.youtube.com/watch?v=42Gtm4-Ax2U')


@bot.command(no_pm=True)
async def gaming():
    await bot.say('https://media1.tenor.com/images/c8827d28f2821f0c78406565f334a6d0/tenor.gif?itemid=9266360')


@bot.command(no_pm=True)
async def k():
    await bot.say('http://i.imgur.com/yyyg94n.gif')


@bot.command(no_pm=True)
async def plumpbois():
    await bot.say('P L U M P B O I S  https://media.giphy.com/media/O5GKT0UDGyQLu/giphy.gif')


@bot.command(pass_context=True, no_pm=True)
async def say(ctx, *args):
    msg = ' '.join(args).format(ctx.message)
    await bot.say(msg)


@bot.command(pass_context=True, no_pm=True)
async def yut(ctx):
    msg = '{0.author.mention} yutted!'.format(ctx.message)
    await bot.say(msg)

# Catch non-existing commands


if __name__ == "__main__":
    check_opus()
    print("Bot on")
    bot.run(config.Config().bot_token)

