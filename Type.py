#using: utf-8
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import os
app = Flask(__name__)

def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

@app.route('/search')
def index():
    return render_template('index.html', len = 0, data = [])

@app.route('/')
def search():
    return render_template('commons/type.html')

@app.route('/station', methods=['GET', 'POST'])
def station():
    IsValue = False
    if request.method == 'POST':
       type = request.form['job']
       print(type)
       if not type:
         IsValue = True
         return render_template('commons/search.html', IsValue = IsValue)
       cur = get_connection().cursor()
       cur.execute('SELECT type,money,place,cando FROM zgundam WHERE type <= %s ORDER BY type ASC', (type,))
       data = cur.fetchall()
       cur.close()
       get_connection().close()
       return render_template('index.html', type = type, data = data, len = len(data))

if __name__ == "__main__":
    app.run()
