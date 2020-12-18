import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('피곤해....'):
        await message.channel.send('ㅇㅈ.....')

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("씨발")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("새끼")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("나쁜새끼")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("썅")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
     await bot.process_commands(message)

client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("년")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("지랄")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("ㅈㄹ")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("씨밸롬")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("씨뷀")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("ㄷㅊ")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

@client.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("ㅆㅂ")
    print(bad)
    if bad >= 0:
        await message.channel.send("바른말 고운말을 사용합시다.") 
        await message.delete()
    await bot.process_commands(message)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
