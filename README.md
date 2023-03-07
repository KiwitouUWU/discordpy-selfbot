# discordpy-selfbot
A discord.py message logger with sqlite database.

## Discord selfbots are against ToS!

### Installation
```
git clone https://github.com/KiwitouUWU/discordpy-selfbot.git discord_bot
cd discord_bot
(create venv if needed)
python setup.py
```

### Usage
1. fill all fields in .env file
    ``DISCORD_TOKEN`` can be a user or bot token, set SELFBOT accordingly.
2. ``python main.py``

### Database structure
(I know just saving the message id in deleted would be better)

logs(guild, guild_id, channel, channel_id, author, userid, time, content)
deleted(guild, guild_id, channel, channel_id, author, userid, time, content)
