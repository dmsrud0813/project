from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def show_games():
    games = list(db.boardGameDB.find({},{'_id':False}))

    return jsonify({'result': 'success', 'game_list': games})


@app.route('/api/zzim', methods=['GET'])
def zzim_games():
    zzim_games = list(db.boardGameDB.find({'like':1},{'_id':False}))

    return jsonify({'result': 'success', 'zzim_list': zzim_games})


@app.route('/api/like', methods=['POST'])
def like_game():
    title = request.form['title']
    game_title = db.boardGameDB.find_one({'title': title})
    if game_title['like']== 0 :
        plus_like = game_title['like']+1
        db.boardGameDB.update_one({'title': title}, {'$set': {'like': plus_like}})
        return jsonify({'result': 'success', 'msg': '좋아요 목록에 추가되었습니다.'})
    else :
        minus_like = game_title['like']-1
        db.boardGameDB.update_one({'title': title}, {'$set': {'like': minus_like}})
        return jsonify({'result': 'success', 'msg': '좋아요 목록에서 삭제되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
