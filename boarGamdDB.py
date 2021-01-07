import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
base_url = 'https://boardlife.co.kr/game_rank.php?tb=&pg='
end_url = '&file=&file2=&view_id='
page_num = 1

new_url = base_url + str(page_num) + end_url
data = requests.get(new_url, headers=headers)
soup = BeautifulSoup(data.text,'html.parser')

game_chart = soup.select('body > table')
#tbody > tr > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1)
print(game_chart)
print(game_chart)
link_tag=[]
for game in game_chart:
        link_tag = game.select_one('tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table#new_game6501 > tbody > tr > td.game_row > table > tbody > tr > td.ellip > a.game_title')
        if link_tag is not None :
            print(link_tag)

