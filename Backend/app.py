from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/challenges', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)