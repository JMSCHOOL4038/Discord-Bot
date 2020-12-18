import asyncio,discord
from discord.ext import commands

token = "Nzg4MjExODIwMzA0MjY5MzQz.X9gNdg.uuPLVcHlT-aXvMWXaomFS2jZqbU"
game = discord.Game("JMSCHOOL (KR)의 도우미 입니다.")
bot = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
	print("봇 시작")

bot.run(token)