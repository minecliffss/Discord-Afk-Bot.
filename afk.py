import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

AFK_CHANNEL_NAME = "┊🇦🇫🇰"  # Name of the AFK channel
MUTE_TIMEOUT_SECONDS = 60  # 1 minutes

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    # Ignore bots
    if member.bot:
        return

    # If the user is muted or self-muted
    if after.self_mute and after.channel is not None:
        await asyncio.sleep(MUTE_TIMEOUT_SECONDS)

        # Check if still muted and still in the same channel
        updated_state = member.voice
        if updated_state and updated_state.self_mute and updated_state.channel == after.channel:
            # Find the AFK channel
            afk_channel = discord.utils.get(member.guild.voice_channels, name=AFK_CHANNEL_NAME)
            if afk_channel:
                await member.move_to(afk_channel)
                print(f"Moved {member.name} to AFK for being muted too long.")
            else:
                print("AFK channel not found.")

bot.run('MTM2NjY0OTU5MTI5ODI2NTE4MQ.Gdt15T.b3wMfdMt2szVyCtS5Ax6MYX2FlyzwQ2KF2lbKE')
