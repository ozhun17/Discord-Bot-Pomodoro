from asyncio import tasks
from cgitb import text
from typing import Text
import discord
import os
import time
import random
from discord.ext import commands
from discord import FFmpegPCMAudio
import timemanagement

client = commands.Bot(command_prefix='pomo')

wasactive = 0
voicechannel = 0
textChannel = 0

@client.event
async def on_ready():
    textChannel = await client.fetch_channel(967347883298914328)
    print('We have logged in as {0.user}'.format(client))




@client.command(pass_context = True)
async def request(ctx):
    if(ctx.author.voice):
        voicechannel = ctx.message.author.voice.channel
    isActive = timemanagement.pomodoroCheck()
    if isActive == 0:
        #request taken
        await ctx.send("request taken")
        wasactive = 1
        timemanagement.pomodoroRequest()



"""@tasks.loop(minutes = 5.0, count=None)
async def pomodorocheck():
    await textChannel.send("Checking pomodoro activity")
    if(timemanagement.pomodoroCheck() == 0):
        await textChannel.send("Pomodoro Not Active.")
        if(wasactive == 1):
            await textChannel.send("Pomodoro done.")
            wasactive = 0
    else:
        await textChannel.send("you have "+ timemanagement.pomodoroCheck()+ " seconds left")
"""
f = open("token", "r")
token = f.readline()
f.close()
#client.run('token')