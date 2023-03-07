from colorama import Fore
from discord.ext import commands


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if type(error) is commands.CommandNotFound:
            pass
        else:
            raise error

    @commands.Cog.listener()
    async def on_ready(self):
        print("\n\n")
        print(Fore.MAGENTA + "[" + Fore.WHITE + '+' + Fore.MAGENTA + "]" + Fore.BLUE + " Connected." + Fore.RESET)


def setup(bot):
    bot.add_cog(general(bot))
