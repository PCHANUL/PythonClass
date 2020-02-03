from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('card-news.html')


@app.route('/test', methods = ['POST'])
def test_post():
    rank_receive = request.form['rank_give']
    rank_receive = int(rank_receive)

    star_receive = request.form['star_give']
    star_receive = int(star_receive)

    db.movies.update_one({'rank':rank_receive},{'$set':{'star':star_receive}})



    return jsonify({'result':'success'})

@app.route('/test', methods = ['GET'])
def test_get():
    rank_receive = request.args.get('rank_give')
    rank_receive = int(rank_receive)
    movie_info = db.movies.find_one({'rank':rank_receive},{'_id':0})

    return jsonify({'result':'success', 'info':movie_info})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)