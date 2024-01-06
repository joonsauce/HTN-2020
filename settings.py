import asyncio
import time
import discord
import os
import requests
import pandas
import json
from discord.ext import commands
import csv
import matplotlib.pyplot as plt
import itertools

prefix = "d!"
description = "Joon's updated version of DisGraph, a HTN 2020++ project and submission by Team Joon."
# csv and xlsx/xls should be enough and most common enough
supported_file_types = [".csv", ".xlsx", ".xls"]

# discord gateway intents
intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=False)

# bot instance
bot = commands.Bot(command_prefix=prefix, intents=intents, description=description, case_insensitive=True,
                   allowed_mentions=allowed_mentions)

