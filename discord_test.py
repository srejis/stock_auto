import discord, asyncio

client = discord.Client()

def import_token():
    token_path = './개인정보/discord_token.txt'
    with open(token_path,'r') as f:
        token = f.read()
    return token

ch = client.get_channel(1313417613799456829)
ch.send ("User, Hello")

@client.event
async def on_ready():
    print("봇이 준비되었습니다!")

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
token = import_token()
client.run(token)
