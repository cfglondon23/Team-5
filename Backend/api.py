from flask import Flask, jsonify, request
from flask_cors import CORS
from Campaign import User, Challenge

app = Flask(__name__)
CORS(app)

citydata = [{'London': {'Numofpoints':'1000'}},
            {'Beijing': {'Numofpoints':'980'}},
            {'Glasgow': {'Numofpoints': '900'}},
            {'Mumbai': {'Numofpoints': '800'}},
            {'Singapore': {'Numofpoints': '700'}},
            {'Tehran': {'Numofpoints': '600'}},
            {'Dubai': {'Numofpoints': '500'}},
            {'Buenos Aires': {'Numofpoints': '400'}}]


@app.route('/userdata', methods=['GET'])
def get_energydata():
    return citydata

@app.route('/challengedata',methods=['GET'])
def get_challengedata():
    return challengedata

if __name__ == '__main__':
    app.run()