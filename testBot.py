import asyncio
import discord
import urllib
import bs4
from urllib.request import urlopen, Request

client = discord.Client()

token = ''
with open('token.txt', 'r') as fp:
    token = fp.readlines()
    fp.close()
token = token[0]

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    #테스트용
    if message.content.startswith('!커맨드'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await channel.send('커맨드') #봇은 해당 채널에 '커맨드' 라고 말합니다.
    if message.content.startswith('!hello'):
        await channel.send('Hello')


    #날씨
    if message.content.startswith('!날씨'): #날씨 입력 할 시
        temp = message.content.split(" ") #split(" ")을 이용해 !날씨 이후의 지역을 받아서 temp에 저장 ex)!날씨 서울 -> 서울의 날씨
        location = temp[1] #지역 저장
        enc_location = urllib.parse.quote(location + '+날씨')

        url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + enc_location #가져올 url 주소

        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'html.parser')
        weather1 = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        weather2 = (soup.find('p', class_='cast_txt').text).split(',')
        embed = discord.Embed(title='날씨', description=location+'날씨 정보 입니다.')
        embed.add_field(name='현재 기온', value=weather1+'℃ 입니다', inline=False)
        embed.add_field(name='상태', value=weather2[0], inline=False)
        embed.add_field(name='비교', value=weather2[1], inline=False)
        await channel.send(embed=embed)
        

    #롤
    if message.content.startswith('!롤'):
        temp = message.content.split(" ")
        name = temp[1]
        enc_location = urllib.parse.quote(name)
        url = 'https://www.op.gg/summoner/userName=' + enc_location
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'html.parser')

        TierRank = soup.find('div', class_='TierRank').text
        lp = soup.find('span', class_='LeaguePoints').text
        lp = lp.strip()

        await channel.send('{0}\n 티어 : {1}\n LP : {2}'.format(name, TierRank, lp))
    #히오스
    if message.content.startswith('!히오스'):
        embed = discord.Embed(title='히오스', description='쓰레기')
        embed.add_field(name='히오스', value='쓰레기')
        await channel.send(embed=embed)

    #메세지창 비우기
    if message.content.startswith('!clear'):
        await message.delete()
        #await channel.send('Clearing messages...')
        async for msg in channel.history():
            #print(msg.id) #메세지 아이디
            await msg.delete()
        await channel.send('Complete Clearing!')


    if message.content.startswith('!도움말' or '!help'):
        temp = message.content.split(" ")
        try:
            if temp[1] is not None:
                if temp[1] == '날씨':
                    await channel.send('!날씨 [지역]을 입력하면 현재 그 지역의 날씨를 알려줍니다.')
                elif temp[1] == '롤':
                    await channel.send('!롤 [닉네임]을 입력하면 해당 닉네임의 티어랭크와 리그포인트를 알려줍니다.')

        except(IndexError, ValueError):
            await channel.send('현재 사용 가능한 명령어는\n'
                               +'!날씨\n'
                               +'!롤\n'
                               +'입니다.')
                              

client.run(token)
