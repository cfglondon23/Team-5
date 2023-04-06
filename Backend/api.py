from flask import Flask, jsonify, request
from flask_cors import CORS
from Campaign import User, Challenge

app = Flask(__name__)
CORS(app)

userdata = [{'Lily':'abc123',
         'Jim':'jpmorgan',
         'Timmy': 'qwert098'}]

challengedata = [{'Turn off lightbulbs!':'10 points',
                  'Turn of TV!':'5 points',
                  "Don't use heating!":'15 points'}]

@app.route('/userdata', methods=['GET'])
def get_energydata():
    return userdata

@app.route('/challengedata',methods=['GET'])
def get_challengedata():
    return challengedata

if __name__ == '__main__':
    app.run(debug=True)