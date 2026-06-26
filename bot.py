import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(
    command_prefix="!",
        intents=intents,
            help_command=None
            )

@bot.event
async def on_ready():
    await bot.tree.sync()

    print("=" * 50)
    print(f"✅ Logged in as {bot.user}")
    print(f"🆔 Bot ID : {bot.user.id}")
    print("💙 Blue Assistant is Online!")
    print("=" * 50)


@bot.tree.command(
name="ping",
description="Check if the bot is online."
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
    f"pong! {round(bot.latency * 1000)}ms"
)

bot.run(TOKEN)