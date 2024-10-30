import os
# import json
from nacl.signing import VerifyKey
# from nacl.exceptions import BadSignatureError
# import asyncio
# import discord
# from discordbot import DiscordBot
from dotenv import load_dotenv


load_dotenv("keys.env")
DISCORD_PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY")


def verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event['params']['header'].get('x-signature-ed25519')
    auth_ts  = event['params']['header'].get('x-signature-timestamp')
    msg = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(DISCORD_PUBLIC_KEY))
    verify_key.verify(msg, bytes.fromhex(auth_sig))

def lambda_handler(event, context):
    print(f"event {event}") # debug print
    try:
        verify_signature(event)
    except Exception as e:
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")
    # body = event.get("body-json")
