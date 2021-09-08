# import requests
# async def create_thread(self,name,minutes,message):
#     token = 'Bot ' + self._state.http.token
#     url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"
#     headers = {
#         "authorization" : token,
#         "content-type" : "application/json"
#     }
#     data = {
#         "name" : name,
#         "type" : 11,
#         "auto_archive_duration" : minutes
#     }
#
#     return requests.post(url,headers=headers,json=data).json()
# discord.TextChannel.create_thread = create_thread
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import json
import os

client = commands.Bot(command_prefix='>>')

@client.event
async def on_ready():
    print('Bot {0.user}  ready'.format(client))

@client.command(name="list")
@has_permissions(manage_channels=True)
async def _list(ctx):
    with open("data.json", "r") as f:
        anjing = json.load(f)
        goblog = anjing[str(ctx.guild.id)]
        await ctx.send("Channel autothread:")
        for channel in goblog:
            await ctx.send(f"<#{channel}>")



@client.command(name="set")
@has_permissions(manage_channels=True)
async def _set(ctx, channel: discord.TextChannel):
    # print("pop")
    with open("data.json", "r") as f:
        anjing = json.load(f)
        goblog = anjing[str(ctx.guild.id)]
        goblog.append(str(channel.id))
        with open("data.json", "w") as f:
            json.dump(anjing, f, indent=4)
            await ctx.send("Udh di add bg 👍")

@client.command(name="remove")
@has_permissions(manage_channels=True)
async def _remove(ctx, channel: discord.TextChannel):
    # print("pop")
    with open("data.json", "r") as f:
        anjing = json.load(f)
        goblog = anjing[str(ctx.guild.id)]
        goblog.remove(str(channel.id))
        # del anjing[str(ctx.guild.id)[channel.id]]
        with open("data.json", "w") as f:
            json.dump(anjing, f, indent=4)
            await ctx.send("Udh di ilangin bg 👍")

@client.event
async def on_guild_join(guild):
    guildid = guild.id
    print(guildid)
    with open("data.json", "r") as f:
        anjing = json.load(f)
        anjing[guildid] = []
        with open("data.json", "w") as f:
            json.dump(anjing, f, indent=4)



for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("token")
