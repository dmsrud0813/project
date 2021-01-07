import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.koreaboardgames.com/boardgame/game_list01.php#pagenum=&view_type=bg&search_sort='

#gameList
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text,'html.parser')

game_chart = soup.select('#gameList')

print(game_chart)

# for game in game_chart:
#         link_tag = game.select_one(
#         if link_tag is not None :
#             print(link_tag)
#
