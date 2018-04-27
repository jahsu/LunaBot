import discord
from configuration import config

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        msg = 'We got no way to help yet {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!wink'):
        msg = 'https://i.fltcdn.net/contents/1754/original_1444280780146_xtv7e23ayvi.gif'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!k'):
        msg = 'http://i.imgur.com/yyyg94n.gif'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!gaming'):
        msg = 'https://media1.tenor.com/images/c8827d28f2821f0c78406565f334a6d0/tenor.gif?itemid=9266360'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!peekaboo'):
        msg = 'https://image.ibb.co/cGzwcc/IU_2.gif'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.Config().bot_token)
