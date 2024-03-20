import discord as discord
from discord.ext import commands
from discord import Message
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("holehe.env")
token = os.getenv("Token")
intents = discord.Intents.default()
intents.message_content = True 
client = commands.Bot(command_prefix = '?', intents = intents)


async def blocking_function(email_address):  
    print('entering blocking function')
    output = subprocess.check_output(['holehe','--only-used',str(email_address)])
    output = output.decode('utf8').replace("'", '"')
    output = output[151:-234].replace("32m[+","HIT FOUND").replace("[32","").replace("[0m","") 
    return output

@client.command(aliases = ["holehe","osint"])
async def OSINT(ctx,message):
    """ Runs holehe against Email in message"""
    if len(message) > 4: #Lazy Error Handle
        email_address = message.replace(" ","").replace(",",".").replace("#","")
        print(email_address)
        output =  await blocking_function(email_address)
        print(output)
    else: 
        output = "Invalid Input"
    await ctx.send(output) #Test ?holehe test@gmail.com
                   
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    

await client.start(token)#client.run(token) if running from non-notebook
