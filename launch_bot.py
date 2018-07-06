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


@bot.command(pass_context=True, no_pm=True, brief="Say hello!", description="Just type !hello")
async def hello(ctx):
    msg = 'Yo whaddup {0.author.mention}'.format(ctx.message)
    await bot.say(msg)

    # if message.content.startswith('!help'):
    #     await client.send_message(message.channel, send_help(message))


@bot.command(no_pm=True, brief="I will welcome you", description="Just type !welcome")
async def welcome():
    await bot.say(commands.welcome.send_welcome())


@bot.command(no_pm=True, brief="See wanted features")
async def feature():
    await bot.say(commands.feature.show_features())


@bot.command(pass_context=True, no_pm=True, brief="Remove bot from current channel")
async def kickbot(ctx):
    bot_music = bot.get_cog('Music')
    for vc in bot.voice_clients:
        if vc.server == ctx.message.server:
            await commands.music.Music.clear_voice_state(bot_music, ctx.message.server)
            return await vc.disconnect()

    return await bot.say("Why you tryin to kick me bruh??")


@bot.command(pass_context=True, no_pm=True, brief="Move bot to requester's channel")
async def move(ctx):
    bot_music = bot.get_cog('Music')
    loc = ctx.message.author.voice_channel
    if loc is None:
        await bot.say('You aint in a channel bruh.')
        return False
    else:
        await commands.music.Music.summon(bot_music, ctx)


@bot.command(no_pm=True, brief=";)")
async def wink():
    await bot.say(commands.wink.wink_iu())


@bot.command(no_pm=True, brief="Try it and find out...")
async def peekaboo():
    await bot.say(commands.peekaboo.peek_iu())


@bot.command(no_pm=True, brief="Yo")
async def gangsta():
    await bot.say(commands.gangsta.gangsta_iu())


@bot.command(pass_context=True, brief="I'll search the wikis", description="ex. !wiki <search_query>")
async def wiki(ctx, *args):
    await bot.say(commands.wiki.query_wiki(ctx, args))


@bot.command(pass_context=True, no_pm=True, brief="I'm twenty five!")
async def twentyfive(ctx):
    url = 'https://www.youtube.com/watch?v=d9IxdwEFk1c'
    bot_music = bot.get_cog('Music')
    player = await commands.music.Music.play_music(bot_music, ctx, url)
    await commands.music.Music.enque(bot_music, ctx, VoiceEntry(ctx.message, player))


@bot.command(pass_context=True, no_pm=True, brief="I'm twenty three!")
async def twentythree(ctx):
    url = 'https://www.youtube.com/watch?v=42Gtm4-Ax2U'
    bot_music = bot.get_cog('Music')
    player = await commands.music.Music.play_music(bot_music, ctx, url)
    await commands.music.Music.enque(bot_music, ctx, VoiceEntry(ctx.message, player))


@bot.command(pass_context=True, no_pm=True, name="420", brief="420 blaze it")
async def fourtwenty(ctx):
    url = 'https://www.youtube.com/watch?v=aVRzocGJzw8'
    bot_music = bot.get_cog('Music')
    player = await commands.music.Music.play_music(bot_music, ctx, url)
    await commands.music.Music.enque(bot_music, ctx, VoiceEntry(ctx.message, player))


@bot.command(pass_context=True, no_pm=True, brief="Play youtube music.", description="ex !play <youtube link>")
async def play(ctx, arg):
    bot_music = bot.get_cog('Music')
    player = await commands.music.Music.play_music(bot_music, ctx, arg)
    await commands.music.Music.enque(bot_music, ctx, VoiceEntry(ctx.message, player))


@bot.command(pass_context=True, no_pm=True, brief="Adjust volume of music player", description="ex. !volume <value>")
async def volume(ctx, arg):
    bot_music = bot.get_cog('Music')
    await commands.music.Music.set_volume(bot_music, ctx, arg)


@bot.command(pass_context=True, no_pm=True, brief="Pause current playing song")
async def pause(ctx):
    bot_music = bot.get_cog('Music')
    await commands.music.Music.pause_player(bot_music, ctx)


@bot.command(pass_context=True, no_pm=True, brief="Resume current  song")
async def resume(ctx):
    bot_music = bot.get_cog('Music')
    await commands.music.Music.resume_player(bot_music, ctx)


@bot.command(pass_context=True, no_pm=True, brief="Stop playing songs")
async def stop(ctx):
    bot_music = bot.get_cog('Music')
    await commands.music.Music.stop_player(bot_music, ctx)


@bot.command(pass_context=True, no_pm=True, brief="Skip your current requested playing song, not others")
async def skip(ctx):
    bot_music = bot.get_cog('Music')
    await commands.music.Music.skip_song(bot_music, ctx)


@bot.command(no_pm=True, brief="Watch me game")
async def gaming():
    await bot.say('https://media1.tenor.com/images/c8827d28f2821f0c78406565f334a6d0/tenor.gif?itemid=9266360')


@bot.command(no_pm=True, brief="Applause")
async def clap():
    await bot.say('https://gfycat.com/SpotlessMedicalAtlanticspadefish')


@bot.command(no_pm=True, brief="K")
async def k():
    await bot.say('http://i.imgur.com/yyyg94n.gif')


@bot.command(no_pm=True, brief="We plump now")
async def plumpbois():
    await bot.say('P L U M P B O I S  https://media.giphy.com/media/O5GKT0UDGyQLu/giphy.gif')


@bot.command(pass_context=True, no_pm=True, brief="Have me say stuff.", description="ex. !say <whatever you want>")
async def say(ctx, *args):
    msg = ' '.join(args).format(ctx.message)
    await bot.say(msg)


@bot.command(pass_context=True, no_pm=True, brief="I'm gonna yut!!!")
async def yut(ctx):
    msg = '{0.author.mention} yutted!'.format(ctx.message)
    await bot.say(msg)


@bot.command(pass_context=True, no_pm=True, brief="Get a blessing")
async def bless(ctx):
    msg = '{0.author.mention} #blessed https://gph.is/2Nn1t1f'.format(ctx.message)
    await bot.say(msg)

# Catch non-existing commands


if __name__ == "__main__":
    check_opus()
    print("Bot on")
    bot.run(config.Config().bot_token)

