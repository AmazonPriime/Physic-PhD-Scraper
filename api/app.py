from flask import Flask
from flask_cors import CORS
from flask import request

from scrapers import scrape_all

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        query = request.get_data(as_text=True)
        jobs = scrape_all()
        print(len(jobs))
        print(jobs[0].export())
        return 'Yay successul POST request! ' + query, 200

    return 'API route only supports POST requests', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
