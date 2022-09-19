from flask import Flask
from flask_cors import CORS
from flask import request
import json
import ast

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        query = request.get_data(as_text=True)
        return 'Yay successul POST request! ' + query, 200

    return 'API route only supports POST requests', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')