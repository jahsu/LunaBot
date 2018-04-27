import discord
from configuration import config
from commands.help import send_help
from commands.welcome import send_welcome
from commands.feature import show_features
from commands.peekaboo import peek_iu
from commands.wink import wink_iu

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Yo whaddup {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        await client.send_message(message.channel, send_help(message))

    if message.content.startswith('!welcome'):
        await client.send_message(message.channel, send_welcome())

    if message.content.startswith('!features'):
        await client.send_message(message.channel, show_features())

    if message.content.startswith('!wink'):
        await client.send_message(message.channel, wink_iu())

    if message.content.startswith('!peekaboo'):
        await client.send_message(message.channel, peek_iu())

    if message.content.startswith('!gaming'):
        msg = 'https://media1.tenor.com/images/c8827d28f2821f0c78406565f334a6d0/tenor.gif?itemid=9266360'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!k'):
        msg = 'http://i.imgur.com/yyyg94n.gif'
        await client.send_message(message.channel, msg)

    # Catch non-existing commands

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.Config().bot_token)
