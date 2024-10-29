import asyncio
import discord
from discordbot import DiscordBot


async def main() -> None:
    dc_client = DiscordBot(intents=discord.Intents.default())
    dc_client.run(dc_client._discord_token)

asyncio.run(main())
