import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import getter
load_dotenv()
print(getter.__file__)
print(dir(getter))
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def play(ctx, target_variable: str):
    if target_variable.startswith("https://www.youtube.com") or target_variable.startswith("youtube.com/"):
        print("here")
        print(getter)
        print(getter.getAudio)
        getter.getAudio(target_variable, ctx.voice_client)
        print("PLAY BOT ID:", id(bot))
        print(bot.voice_clients)
    else:
        await ctx.send("this aint a youtube link king", ephemeral=True, silent=True)



@bot.command()
async def connect(ctx):
     if ctx.author.voice:
         channel = ctx.author.voice.channel
         await channel.connect()
         print("CONNECT BOT ID:", id(bot))
         print(bot.voice_clients)
     else:
         await ctx.send("join a call king", ephemeral=True, silent=True)

@bot.command()
async def disconnect(ctx):
         await ctx.voice_client.disconnect()

@bot.event
async def on_voice_state_update(member, before, after):
    for vc in bot.voice_clients:
        if vc.channel:
            people = [m for m in vc.channel.members if not m.bot]

            if len(people) == 0:
                await vc.disconnect()



bot.run(token, log_handler=handler, log_level=logging.DEBUG)
