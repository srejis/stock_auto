import discord, asyncio

client = discord.Client()

def import_token():
    token_path = './개인정보/discord_token.txt'
    with open(token_path,'r') as f:
        token = f.read()
    return token

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("메세지 보내는 봇"))

@client.event
async def on_message(message):
    if message.content == "test": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content == "무요":
        await message.channel.send ("무요 멀바요")

    if message.content == "우쩔":
        await message.channel.send ("우쩔우쩔!!")

    if message.content == "메롱":
        await message.channel.send ("메메롱 메롱!")


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
token = import_token()
client.run(token)