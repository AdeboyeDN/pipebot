import os
import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"Welcome to the server, {member.mention}!")

token = os.getenv("BOT_TOKEN")

client.run(token)
