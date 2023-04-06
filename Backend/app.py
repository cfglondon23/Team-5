from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = [{"test":"yes", "hello":"world"}]

@app.route('/challenges')
def webpage():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)