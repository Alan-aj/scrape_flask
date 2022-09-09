import sqlite3

def addData(articles):
    try:
        db=sqlite3.connect('scrape.db')
        print("db connect")
        cur=db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS article (id INTEGER PRIMARY KEY AUTOINCREMENT, url CHAR, headline CHAR, author CHAR, date DATE );")
        qry="insert into article (url, headline, author, date) values(?,?,?,?);"
        for article in articles:
            cur.execute(qry, (article["url"], article["headline"], article["author"], article["date"]))
            db.commit()
    except Exception as e:
        print("error in operation - ",e)
    finally:
        db.close()
