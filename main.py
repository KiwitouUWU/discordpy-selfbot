from discord.ext import commands
import os
from dotenv import load_dotenv
from colorama import Fore


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SELFBOT = os.getenv('SELFBOT')

bot = commands.Bot(command_prefix="") # no actual commands will be called


for extension in os.listdir("cogs/"):
    if not extension in ["__pycache__"]:
        try:
            bot.load_extension("cogs."+str(extension)[:-3])
            print(Fore.GREEN + "Cog \"" + str(extension)[:-3] + "\" succesfully loaded." + Fore.RESET)
        except Exception as e:
            print(Fore.RED + "Cog \"" + str(extension)[:-3] + "\" couldnt be loaded." + Fore.RESET)
            print(e)


bot.run(TOKEN, bot=False if SELFBOT == "True" or SELFBOT== "true" else True)

