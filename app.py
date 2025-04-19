import os
from flask import Flask
from datetime import date
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("MY_NAME", "Ferko")
    return f"<h1 style='color:blue'>Hello There {name}!</h1>"

@app.route("/date")
def today():
    today = date.today()
    return f"<p>{today.strftime('%d.%m.%Y')}</p>"

@app.route("/connect")
def connect():
    if "POSTGRES_HOST" in os.environ:
        host = os.environ["POSTGRES_HOST"]
        connection = psycopg2.connect(host)
        cur = connection.cursor()
        cur.execute("SELECT * FROM vendors;")
        rows = cur.fetchall()
        cur.close()
        connection.close()
        return f"<h1 style='color:blue'>{rows}!</h1>"
    return "<h1 style='color:red'>No host provided!</h1>"

if __name__ == "__main__":
    app.run()
