import asyncio
import discord
import urllib
import bs4
from urllib.request import urlopen, Request

client = discord.Client()

token = "NjAxMzg1Nzg3MDYxMTc0MzEw.XTBmrA.QjJKCWJXZ9ToP8ilvw0aO8rcXyw"

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

    if message.content.startswith('!커맨드'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await channel.send('커맨드') #봇은 해당 채널에 '커맨드' 라고 말합니다.
    if message.content.startswith('!hello'):
        await channel.send('Hello')


    if message.content.startswith('!날씨'): #날씨 입력 할 시
        temp = message.content.split(" ") #split(" ")을 이용해 !날씨 이후의 지역을 받아서 temp에 저장 ex)!날씨 서울 -> 서울의 날씨
        location = temp[1] #지역 저장
        enc_location = urllib.parse.quote(location + '+날씨')

        url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + enc_location #가져올 url 주소

        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'html5lib')
        await channel.send('현재 {0} 날씨는 {1}도 입니다.'.format(location, (soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text)))
        
client.run(token)
