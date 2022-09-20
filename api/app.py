from flask import Flask
from flask_cors import CORS
from flask import request
import json

from scrapers import scrape_all

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        query = request.get_data(as_text=True)
        jobs = scrape_all()
        jobs = [job.export() for job in jobs]
        return json.dumps(jobs), 200

    return 'API route only supports GET requests', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
