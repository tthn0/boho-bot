from classes import *

import os


class Bot(commands.Bot):
    async def on_ready(self):
        print("Logged on as", self.user)

    def load_cogs(self):
        for file in os.listdir("src/cogs"):
            if file.endswith(".py"):
                self.load_extension(f"cogs.{file[:-3]}")


def main():
    bot: commands.Bot = Bot(
        command_prefix=commands.when_mentioned,
        intents=discord.Intents.all(),
        help_command=None,
    )
    bot.load_cogs()
    bot.run(CONSTANTS.TOKEN)


if __name__ == "__main__":
    main()
