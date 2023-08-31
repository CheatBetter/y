"""
Copyright 2023 CheatBetter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Join Us
"""
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.slash_command()
async def status (ctx):
    await ctx.author.send("**Status of the bot:** null__Watching__ Roblox Altsnull**What the `/restock` command does**nullThe bot will request a txt file in the format with the accounts in the format 'username:password'. The bot will detect the usernames and password and seperate them or whatever. This is what will be sent to a user when they use the command below. Each account can only be sent once, and will get deleted from the list of accounts sent to the user.null**What the `/alt-gen` command does:**nullThe bot will send an embed DM to the user who ran the command, and give them the username & password. There will be a cooldown of 10 minutes between each time the command is ran. The embed should be similar to the one below. (I don't mind if it's just the username and password, without any PFPs, etc - but it'd be better if the extra info was included)null")

bot.run("")
