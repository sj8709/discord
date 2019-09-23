import asyncio
import discord
import urllib
import bs4
from urllib.request import urlopen, Request
import re
'''
a = input()
temp = a.split(" ")
location = temp[1]
enc_location = urllib.parse.quote(location + '+날씨')
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + enc_location #가져올 url 주소

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html, 'html5lib')

print('{0}, {1}'.format(location, (soup.find('p', class_='cast_txt').text)))
print('{0}, {1}'.format(location, (soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text)))
print('{0}, {1}'.format(location, (soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text)))


name = input()
enc_location = urllib.parse.quote(name)
url = 'https://www.op.gg/summoner/userName=' + enc_location #가져올 url 주소

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html, 'html5lib')


print('{0}님의'.format(name))
print('티어는 {0}'.format(soup.find('div', class_='TierRank').text))
lp = soup.find('span', class_='LeaguePoints').text
lp = lp.strip()
print('{0}'.format(lp))
'''
token = ''
with open('token.txt', 'r') as fp:
    token = fp.readlines()
    token = token[0]

print(token)
