from flask import *
from scrape.scrape import job

app = Flask(__name__)

@app.route('/')
def home():
    data = job()
    print(data)
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run()