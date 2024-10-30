import boto3
import json
import os
import requests


AWS_ACCESS_KEY_ID       = os.environ.get("AWS_IAM_USER_PK")
AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_IAM_USER_SK")
AWS_REGION              = os.environ.get("AWS_REGION")
AWS_BUCKET              = os.environ.get("AWS_BUCKET")
KEY                     = 'alpaca.json'

BROKER_API_KEY          = os.getenv("BROKER_API_KEY")
BROKER_SECRET_KEY       = os.getenv("BROKER_SECRET_KEY")

DISCORD_APPLICATION_ID  = os.getenv("DISCORD_APPLICATION_ID")
DISCORD_BOT_TOKEN       = os.getenv("DISCORD_BOT_TOKEN")
TEST_SERVERS            = json.loads(os.environ.get("TEST_SERVERS"))

HTTP_HEADER = {"Authorization": f"Bot {DISCORD_BOT_TOKEN}"}

# form the APi endpoints: https://discord.com/developers/docs/interactions/slash-commands#registering-a-command
global_url = f"https://discord.com/api/v8/applications/{DISCORD_APPLICATION_ID}/commands"
guild_urls = [f"https://discord.com/api/v8/applications/{DISCORD_APPLICATION_ID}/guilds/{test_server_id}/commands" for test_server_id in TEST_SERVERS]

s3 = boto3.client(
        "s3",             
        aws_access_key_id=AWS_ACCESS_KEY_ID, 
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
        region_name=AWS_REGION
)


def get_json(bucket, key):
    res = s3.get_object(Bucket=bucket, Key=key)
    try:
        text = res["Body"].read().decode()
    except Exception as e:
        print(f"err: no file found at {bucket}/{key}: {e}")
    return json.loads(text)

def get_all_commands(url):
    existing_commands = requests.get(url, headers=HTTP_HEADER).json()
    if not existing_commands:
        return []

def delete_command(url):
    r = requests.delete(url, headers=HTTP_HEADER)
    print(r.text)

def post_command(url, commands):
    r = requests.post(url, headers=HTTP_HEADER)
    if r.status_code != 200:
        r = requests.post(url, headers=HTTP_HEADER, json=commands)
    print(f"Response from {url}: {r.text}")

def run():
    # use guild_urls to test, since global changes take effect after a delay
    # optional: delete all existing commands to reset to clean state
    # for guild_url in guild_urls:
    #    for command in get_all_commands(guild_url):
    #        delete_command(f"{guild_url}/{command['id']}")
            
    # publish new commands
    commands = get_json(AWS_BUCKET, KEY)
    for url in guild_urls:
        for command in commands:
            post_command(url, command)

    # uncomment to publish globally
    # for command in commands:
    #     publish_command(global_url, command)

    print(f"{len(commands)} published")

    
if __name__ == "__main__":
    run()