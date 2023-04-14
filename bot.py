import os
import discord
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    # Send a greeting message to the member
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"Welcome to the server, {member.mention}!")


#client.run(os.getenv('BOT_TOKEN'))
client.run(os.getenv('BOT_NEW_TOKEN'))
