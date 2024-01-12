import asyncio
import csv
import discord
import itertools
import matplotlib.pyplot as plt
import os
import pandas
import requests
import uuid
from functools import reduce
from discord.ext import commands

prefix = "d!"
description = "Joon's updated version of DisGraph, a HTN 2020++ project and submission by Team Joon."
# csv and xlsx/xls should be enough and most common enough
supported_file_types = [".csv", ".xlsx", ".xls"]

# for debug only, find exactly what intents are required
intents = discord.Intents.all()
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=False)

# bot instance
bot = commands.Bot(command_prefix=prefix, intents=intents, description=description, case_insensitive=True,
                   allowed_mentions=allowed_mentions)

# remove help command to add custom help command
bot.remove_command('help')

# gets bot token from text file
with open('bot_token.txt', 'r') as token:
    bot_token = token.readline()


# check that bot is ready to work
@bot.event
async def on_ready():
    print("Status: OK")

