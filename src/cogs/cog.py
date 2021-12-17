from classes import *

import random


class Cog(commands.Cog):
    def __init__(self, client):
        self.client: discord.Client = client

    @commands.Cog.listener()
    async def on_connect(self):
        await self.client.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="BOHO BONES",
            ),
        )

        self.guild: discord.Guild = self.client.get_guild(CONSTANTS.GUILD_ID)
        self.members: list[discord.Member] = list()
        self.channel: discord.TextChannel = await self.client.fetch_channel(
            CONSTANTS.CHANNEL_ID
        )

        self.callouts.start()

    @tasks.loop(hours=4)
    async def callouts(self):
        while True:
            try:
                random_member: discord.Member = self.members.pop(
                    random.randrange(len(self.members))
                )
                await self.channel.send(random_member.mention)
            except ValueError:
                self.members: list[discord.Member] = [
                    member for member in self.guild.members if not member.bot
                ]
                continue
            break


def setup(client):
    client.add_cog(Cog(client))
