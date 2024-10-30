import os

import discord
from discord.ext import tasks
from dotenv import load_dotenv


class DiscordBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv("keys.env")
        self._discord_token = os.getenv("DISCORD_BOT_TOKEN")
        self._channel_id = int(os.getenv("CHANNEL_ID"))

    async def setup_hook(self) -> None:
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=60)
    async def my_background_task(self):
        await self.wait_until_ready()  # wait until the bot logs in
        channel = self.get_channel(self._channel_id)  # channel ID goes here
        self.counter += 1
        await channel.send(self.counter)
