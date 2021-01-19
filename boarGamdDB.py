import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.koreaboardgames.com/_proc/get_products_list.php'

page_num = 1

for i in range(62):
    data = {'pagenum': page_num, 'view_type': 'bg'}
    chart = requests.post(url, data).json()['rows']
    chart_num = 0
    for i in range(10):
        game_title = chart[chart_num]['prd_name']
        gmae_player = chart[chart_num]['game_pers']
        game_playtime = chart[chart_num]['game_time']
        game_thumbnail = chart[chart_num]['img'].replace('<','')
        game_thubnail2= game_thumbnail.replace('height="230"','')
        game_thumbnail3 = game_thubnail2.replace('>','')
        game_thumbnail4 = game_thumbnail3.replace('img src=','')
        thumbnail = game_thumbnail4.replace('"','')
        game_id=chart[chart_num]['idx']
        game_url = 'https://www.koreaboardgames.com/boardgame/game_view.php?prd_idx='+ game_id
        detail_data = requests.get(
            game_url,
           headers=headers)
        soup = BeautifulSoup(detail_data.text, 'html.parser')
        game_category = soup.select_one('#container > div.gameDetail > div.gameInfo > div.innerbox > div.infoBox > ul:nth-child(2) > li:nth-child(6)')
        if game_category is not None :
            category = game_category.text
        else :
            category = 'none'
        doc = {
            'title': game_title,
            'player': gmae_player,
            'playtime': game_playtime,
            'img_url': thumbnail,
            'catetory': category,
            'like': 0
        }
        db.boardGameDB.insert_one(doc)
        print('완료!', game_title)
        chart_num = chart_num + 1;
    page_num = page_num+1




