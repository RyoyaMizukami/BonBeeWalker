#using: utf-8
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import os
app = Flask(__name__)

def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

cur = get_connection().cursor()
cur.execute('SELECT * FROM zgundam ORDER BY id ASC')
data = cur.fetchall()
cur.close()
get_connection().close()

@app.route('/')
def index():
    return render_template('index.html', len = len(data), data = data)


if __name__ == "__main__":
    app.run()
