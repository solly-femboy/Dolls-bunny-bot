import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# Keep bot alive
app = Flask('')

@app.route('/')
def home():
    return "Bot is running"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is online and ready, doll 💗")

@bot.command()
async def done(ctx):
    responses = [
        f"Good job, doll. Your thighs thanked you today 💞",
        f"Consistency is how you bloom, doll 🩷",
        f"Your softness is growing beautifully 🩵",
        f"One step closer to plush bunny hips 💗🐰",
    ]
    await ctx.send(responses[os.urandom(1)[0] % len(responses)])

keep_alive()
token = os.getenv("TOKEN")
bot.run(token)
