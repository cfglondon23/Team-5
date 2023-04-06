from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = [{"test":"yes", "hello":"world"}]

@app.route('/challenges', methods=['GET'])
def get_data():
    return data


if __name__ == '__main__':
    app.run(debug=True)