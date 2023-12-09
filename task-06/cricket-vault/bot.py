from scraper import getScore
from scraper import getScores
import os
import pandas as pd
import discord
import requests
import json
from bs4 import BeautifulSoup
const config = require('./config.json');

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    commands = ["/livescore","/generate","/help"]
    if message.content.startswith("/help"):
        await message.channel.send("Available Commands: \n")
        for i in commands:
            await message.channel.send(i)
    elif message.content.startswith("/livescore"):
        scoreboard = getScore()
        if len(scoreboard) == 0:
            await message.channel.send("No Live Matches!!!")
        else: 
            await message.channel.send(scoreboard[2])
            
            await message.channel.send(scoreboard[0] + " => " + scoreboard[3])
            try:
                await message.channel.send(scoreboard[1] + " => " + scoreboard[4])
            except IndexError:
                await message.channel.send(scoreboard[1] + " =>  yet to bat")
    elif message.content.startswith('/generate'):
        try:
            csv_data = pd.read_csv('scores.csv')
        except FileNotFoundError:
            await message.channel.send('CSV file not found.')
            return
        csv_string = csv_data.to_string(index=False)
        await message.channel.send(f'```\n{csv_string}\n```')

client.run(config.token)
