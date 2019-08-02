import discord
from discord.ext import commands

startup_extensions = {"Music"}
bot = commands.Bot(".")

#read_token, obviously
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
    return lines[0].strip()

#begins the bot
@bot.event
async def on_ready():
    print('Logging in as R2-D2')
    print("R2D2 is now online")
    print("..................")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extensions(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


token = read_token()
bot.run(token, reconnect=True)

