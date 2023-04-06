from flask import Flask, jsonify, request
from flask_cors import CORS
#from Campaign import User, Challenge

app = Flask(__name__)
CORS(app)

citydata = [{'City':'London', 'Numofpoints':'1000','Rank':'1'},
            {'City':'Beijing', 'Numofpoints':'980','Rank':'2'},
            {'City':'Glasgow', 'Numofpoints': '900','Rank':'3'},
            {'City':'Mumbai', 'Numofpoints': '800','Rank':'4'},
            {'City':'Singapore', 'Numofpoints': '700','Rank':'5'},
            {'City':'Tehran', 'Numofpoints': '600','Rank':'6'},
            {'City':'Dubai', 'Numofpoints': '500','Rank':'7'},
            {'City':'Shanghai', 'Numofpoints': '400','Rank':'8'},
            {'City':'Cardiff', 'Numofpoints': '300','Rank':'9'}]

challengedata = [{'Challenge1':{'Name':'Earth Hour',
                                'Duration':'1',
                                'Reward':'3'}},
                {'Challenge2':{'Name':'Zero Waste',
                                'Duration':'1',
                                'Reward':'3'}},
                {'Challenge3':{'Name':'Greenify Your Life',
                                'Duration':'1',
                                'Reward':'3'}},
                {'Challenge4':{'Name':'Eco-Friendly',
                                'Duration':'1',
                                'Reward':'3'}},
                {'Challenge5':{'Name':'Carbon Footprint',
                                'Duration':'1',
                                'Reward':'3'}},
                {'Challenge6':{'Name':'Reduce, Reuse, Recycle',
                                'Duration':'1',
                                'Reward':'3'}}]

@app.route('/userdata', methods=['GET'])
def get_energydata():
    return citydata

@app.route('/challengedata',methods=['GET'])
def get_challengedata():
    return challengedata

if __name__ == '__main__':
    app.run()