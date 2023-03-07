import os
import sqlite3
import sys

print("Installing dependencies...")
os.system(f"{sys.executable} -m pip install -r requirements.txt")

from dotenv import load_dotenv
load_dotenv()

print("Creating database...")
conn = sqlite3.connect(os.getenv("DATABASE_FILE"))
c = conn.cursor()
c.execute(
    "create table logs(" +
    "message_id nvarchar(4000)," +
    "guild nvarchar(4000)," +
    "guild_id nvarchar(4000)," +
    "channel nvarchar(4000)," +
    "channel_id nvarchar(4000)," +
    "author nvarchar(4000)," +
    "userid nvarchar(4000)," +
    "time nvarchar(4000)," +
    "content nvarchar(4000)," +
    "url nvarchar(4000)," +
    "attachment nvarchar(4000)" +
    ");"
) # i am aware that this is inefficient but who cares
c.execute(
    "create table deleted(" +
    "message_id nvarchar(4000)," +
    "guild nvarchar(4000)," +
    "guild_id nvarchar(4000)," +
    "channel nvarchar(4000)," +
    "channel_id nvarchar(4000)," +
    "author nvarchar(4000)," +
    "userid nvarchar(4000)," +
    "time nvarchar(4000)," +
    "content nvarchar(4000)," +
    "url nvarchar(4000)," +
    "attachment nvarchar(4000)" +
    ");"
)
conn.commit()
conn.close()
print("Done")
