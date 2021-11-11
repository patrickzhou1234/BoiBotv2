import os
import emoji
import discord
from dotenv import load_dotenv
from discord.ext import commands

#uptimerobot webserver
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is online"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

#real bot code

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def delete(ctx, arg):
    limit = int(arg)
    await ctx.channel.purge(limit=limit)

@bot.command()
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)

@bot.event
async def on_message_delete(message):
  await message.channel.send(str(message.author)+" deleted his message '"+message.content+"'")

@bot.event
async def on_message_edit(message_before, message_after):
        author = message_before.author
        guild = message_before.guild.name
        channel = message_before.channel


        await channel.send(f"""{author} edited his original message: '{message_before.content}' to an Edited Message: '{message_after.content}'""")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "emo" in message.content:
        await message.reply("EMO CHICK https://open.spotify.com/album/37CqAwxTungNxKpIK5vSgE")

    if "post malone" in message.content:
        await message.reply("keep listening to him or die.")

    if bot.user.mentioned_in(message):
        await message.channel.send('Dont ping me or.')

    if emoji.emoji_count(message.content) > 0:
        await message.reply('@'+str(message.author)+' One more time and its a ban. NO EMOJIS')

    if "patrick" in message.content:
        await message.reply('YAH creator of boi botv2')

    if "zaky" in message.content:
        await message.reply('all hail the king')

    if "hurt" in message.content or "ouch" in message.content:
        await message.reply(file=discord.File('hurted.mp4'))
    
    await bot.process_commands(message)

keep_alive()
bot.run(TOKEN)
