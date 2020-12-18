import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("ㅈㄹ")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

client.run('Nzg4MjExODIwMzA0MjY5MzQz.X9gNdg.uuPLVcHlT-aXvMWXaomFS2jZqbU')