import os
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    # Send a greeting message to the member
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"Welcome to the server, {member.mention}!")



client.run(os.getenv('BOT_TOKEN'))