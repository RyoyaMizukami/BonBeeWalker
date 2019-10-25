#using: utf-8
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import os
app = Flask(__name__)

def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

@app.route('/')
def index():
    return render_template('index.html', len = 0, data = [])

@app.route('/search')
def search():
    return render_template('commons/search.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    IsValue = False
    if request.method == 'POST':
       budget = request.form['budget']
       print(budget)
       if not budget:
         IsValue = True
         return render_template('commons/search.html', IsValue = IsValue)
       cur = get_connection().cursor()
       cur.execute('SELECT * FROM zgundam WHERE money <= %s ORDER BY money ASC', (budget,))
       data = cur.fetchall()
       cur.close()
       get_connection().close()
       return render_template('index.html', budget = budget, data = data, len = len(data))

if __name__ == "__main__":
    app.run()
