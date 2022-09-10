from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    return f'Last scraped on {d1}'

if __name__ == '__main__':
    app.run()