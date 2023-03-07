import os
import sqlite3
import discord
from discord.ext import commands
from colorama import Fore
import json


class db_logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.output = True
        self.colorswitch = False # this swaps between true and false. no turning off lmao
        self.last_message = 69420 # random number, doesnt matter

    async def _execute_sql(self, query, args):
        conn = sqlite3.connect(os.getenv("DATABASE_FILE"))
        c = conn.cursor()
        c.execute(query, args)
        conn.commit()
        conn.close()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        Store all cached messages that get deleted in "deleted", this will create dublicates.
        This will NOT be able to access non-cached messages. This is due to intent conflicts with the discord user API.
        Use on_raw_message_delete instead if you need it. https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_raw_#discord.on_raw_message_delete

        To filter all remaining messages, just use the following sql query:
        SELECT * FROM logs EXCEPT SELECT * FROM deleted
        """
        async for m in message.channel.history(limit=1):
            message = m
        if message.author.bot:
            return
        if self.last_message == message.id:
            return
        self.last_message = message.id
        author = None
        content = None
        userid = None
        time = None
        guild_id = None
        guild = None
        channel_id = None
        channel = None
        jump_url = None
        try:
            author = str(message.author)
        except:
            pass
        try:
            content = str(message.content)
        except:
            pass
        try:
            userid = str(message.author.id)
        except:
            pass
        try:
            time = str(message.created_at)
        except:
            pass
        try:
            guild_id = str(message.guild.id)
        except:
            pass
        try:
            guild = str(message.guild)
        except:
            pass
        try:
            channel_id = str(message.channel.id)
        except:
            pass
        try:
            channel = str(message.channel)
        except:
            pass
        message_id = None
        try:
            message_id = str(message.id)
        except:
            pass
        try:
            jump_url = str(message.jump_url)
        except:
            pass
        if len(message.attachments) > 0:
            pic_urls = [pic.url for pic in message.attachments]
            attachment = json.dumps(pic_urls)
        else:
            attachment = None
        row = [message_id, guild, guild_id, channel, channel_id, author, userid, time, content, jump_url, attachment]
        await self._execute_sql("INSERT INTO deleted VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

        # print console message
        if self.colorswitch:
            if message.channel.type == discord.ChannelType.private:
                prefix = Fore.LIGHTGREEN_EX + "(DM) "
            else:
                prefix = Fore.LIGHTMAGENTA_EX + "(GUILD) "
            print(Fore.LIGHTRED_EX + "[Logger] " + prefix + Fore.LIGHTRED_EX + "Message deleted -> " + message.author.name + "#" + message.author.discriminator + ": " + message.content + Fore.RESET)
        else:
            if message.channel.type == discord.ChannelType.private:
                prefix = Fore.GREEN + "(DM) "
            else:
                prefix = Fore.MAGENTA + "(GUILD) "
            print(Fore.RED + "[Logger] " + prefix + Fore.RED + "Message deleted -> " + message.author.name + "#" + message.author.discriminator + ": " + message.content + Fore.RESET)
        self.colorswitch = not self.colorswitch

    @commands.Cog.listener()
    async def on_message(self, message):
        async for m in message.channel.history(limit=1):
            message = m
        if self.last_message == message.id:
            return
        if message.author == self.bot.user:
            return
        self.last_message = message.id
        author = None
        content = None
        userid = None
        time = None
        guild_id = None
        guild = None
        channel_id = None
        channel = None
        jump_url = None
        message_id = None
        try:
            message_id = str(message.id)
        except: pass
        try:
            author = str(message.author)
        except: pass
        try:
            content = str(message.content)
        except: pass
        try:
            userid = str(message.author.id)
        except: pass
        try:
            time = str(message.created_at)
        except: pass
        try:
            guild_id = str(message.guild.id)
        except: pass
        try:
            guild = str(message.guild)
        except: pass
        try:
            channel_id = str(message.channel.id)
        except: pass
        try:
            channel = str(message.channel)
        except:
            pass
        try:
            jump_url = str(message.jump_url)
        except:
            pass
        if len(message.attachments) > 0:
            pic_urls = [pic.url for pic in message.attachments]
            attachment = json.dumps(pic_urls)
        else:
            attachment = None
        row = [message_id, guild, guild_id, channel, channel_id, author, userid, time, content, jump_url, attachment]
        await self._execute_sql("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

        # print console message
        if self.output:
            if message.author.bot:
                print(Fore.LIGHTBLACK_EX + "[Logger] " + Fore.LIGHTBLACK_EX + "(Bot) " + Fore.LIGHTBLACK_EX + message.author.name + "#" + message.author.discriminator + ": " + message.content + Fore.RESET)
            else:
                if self.colorswitch:
                    if message.channel.type == discord.ChannelType.private:
                        prefix = Fore.LIGHTGREEN_EX + "(DM) "
                    else:
                        prefix = Fore.LIGHTMAGENTA_EX + "(GUILD) "
                    print(Fore.LIGHTBLUE_EX + "[Logger] " + prefix + Fore.LIGHTMAGENTA_EX + message.author.name + "#" + message.author.discriminator + ": " + message.content + Fore.RESET)
                else:
                    if message.channel.type == discord.ChannelType.private:
                        prefix = Fore.GREEN + "(DM) "
                    else:
                        prefix = Fore.MAGENTA + "(GUILD) "
                    print(Fore.BLUE + "[Logger] " + prefix + Fore.MAGENTA + message.author.name + "#" + message.author.discriminator + ": " + message.content + Fore.RESET)
                self.colorswitch = not self.colorswitch


def setup(bot):
    bot.add_cog(db_logger(bot))
