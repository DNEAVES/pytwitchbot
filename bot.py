#!/usr/bin/env python3

from twitchio.ext import commands
from keyboard import press_and_release as keypress
import PySimpleGUI as psgui #Only needed if you want a small window to show up, ensuring the bot is running. Unnecessary if running straight from a terminal.

#SuperSecretTwitchStuff
TMI_TOKEN= #insert
CLIENT_ID= #your
BOT_NICK= #stuff
CHANNEL= #here

#This only exists to wake up the keyboard module
keypress('shift')

class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(irc_token=TMI_TOKEN, client_id=CLIENT_ID, nick=BOT_NICK, prefix="!", initial_channels=[CHANNEL])

    async def event_ready(self):
        print(f"{BOT_NICK} is ready!")

    #Make sure the bot is awake and in the right place
    @commands.command(name='test')
    async def test(self, ctx):
        if ctx.author.name.lower() == "": #Insert approved user between the quotes
            await ctx.send("Test Successful! Hello!")
        else:
            await ctx.channel.send("Sorry, you're not allowed to use this bot!")

    #Basic  to send a keypress on a command. Can check if a user is approved or not.
    @commands.command(name='') #Insert command name between the ticks
    async def scenegame(self, ctx):
        if ctx.author.name.lower() == "": #Insert approved user between the quotes
            keypress('shift+F9') #Replace with desired keyboard shortcut. Refer to the python keyboard documentation for appropriate keys.
            await ctx.channel.send("Job's done!")
            #Unusual bug with the keyboard module, we will send the keypress a second time to make sure it works.
            keypress('shift+F9') #Once again, replace keyboard shortcut
        else:
            await ctx.channel.send("Sorry, you're not allowed to use this bot!")

#Run the bot
bot = Bot()
bot.run()

#A small window to ensure users running this command as a pre-packaged program know the program is running. Redundant if run straight from a terminal, and can be removed.
layout = [[psgui.Text("Bot is running!")]]
psgui.theme('dark purple 1')
window = psgui.Window('TwitchBot', layout)
