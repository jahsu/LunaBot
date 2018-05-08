import asyncio
from discord.ext import commands as cmd


class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()


class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    async def clear_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is not None:
            self.voice_states = {}

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    async def summon(self, ctx):
        loc = ctx.message.author.voice_channel
        if loc is None:
            await self.bot.say('Get in a channel bruh.')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(loc)
        else:
            await state.voice.move_to(loc)

        return True

    async def play_music(self, ctx, url: str):
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await self.summon(ctx)
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(url, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            await self.bot.say('cant play ur jams')
            print(e)
        else:
            player.volume = 0.1
            return player

    async def set_volume(self, ctx, vol: int):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = vol / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))

    async def pause_player(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()

    async def resume_player(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    async def stop_player(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[ctx.message.server.id]
            await state.voice.disconnect()
        except:
            pass

    async def skip_song(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('No tunes up in here bruh.')
            return

        if ctx.message.author == state.current.requester:
            await self.bot.say("Moving to better songs....")
            state.skip()
        else:
            await self.bot.say('Wait your turn, bruh.')

    async def enque(self, ctx, entry):
        state = self.get_voice_state(ctx.message.server)
        await state.songs.put(entry)
