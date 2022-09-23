from datetime import datetime
import discord
import dotenv
import os

INTENTS = discord.Intents.all()
HELP_LIST = [
    ["play `連結 or 關鍵字`", "播放音樂"],
    ["pause","暫停音樂"],
    ["resume","取消暫停音樂"],
    ["skip","跳過音樂"],
    ["queue","查看播放清單"],
    ["clearqueue","清空播放清單"],
    ["dc","中斷連線"],
    ["np","查看正在播放的音樂資訊"]
]

bot = discord.Bot(command_prefix="!",intents=INTENTS)

bot.load_extension(name="music")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Some Music 指令介紹",
        color=discord.Colour.random(),
        timestamp=datetime.utcnow()
    )

    for list in HELP_LIST:
        embed.add_field(name=list[0],value=list[1])
    
    await ctx.respond(embed=embed)

@bot.event
async def on_ready():
    print("bot is ready!")

if __name__ == "__main__":
    dotenv.load_dotenv()
    bot.run(os.getenv("TOKEN"))
