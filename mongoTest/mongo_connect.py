from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'easbdt'
app.config['MONGO_URI'] ='mongodb://didin:didin@cluster0-shard-00-00-cgiec.mongodb.net:27017,cluster0-shard-00-01-cgiec.mongodb.net:27017,cluster0-shard-00-02-cgiec.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'

mongo = PyMongo(app)
@app.route('/add')
def add():
    user = mongo.db.profil
    # user.insert({'name' : 'Didin'})
    # profil = user.find_one({'name': 'Didin'})
    # profil['Foods'] = ['tempe']
    # user.save(profil)
    user.update_one({'name':'Didin'},{'$push':{'Drinks':'Juice Mangga','Foods':'pentol'}})
    return 'update Data!'


if __name__ == '__main__':
    app.run(debug=True)