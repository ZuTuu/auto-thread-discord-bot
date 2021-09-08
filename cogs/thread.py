import requests
async def create_thread(self,name,minutes,message):
    token = 'Bot ' + self._state.http.token
    url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"
    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }

    return requests.post(url,headers=headers,json=data).json()

import discord
from discord.ext import commands
import json
import os
discord.TextChannel.create_thread = create_thread

class thread(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        with open("data.json", "r") as f:
            data = json.load(f)
            goblog = data[str(ctx.guild.id)]
            chan = ctx.channel.id
            # print(ctx.channel.id)
            # print(data.keys())
            if f"{chan}" not in goblog:
                return
            else:
                if ctx.content == "":
                    nama = "Sebuah thread"
                else:
                    nama = ctx.content
                await ctx.channel.create_thread(name=nama, minutes=60, message=ctx)

def setup(client):
    client.add_cog(thread(client))
