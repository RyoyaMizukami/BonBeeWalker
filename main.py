#using: utf-8
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import os
app = Flask(__name__)
API_key = os.environ.get('gmap_API')

def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

def create_pulldown_menu():
    cur = get_connection().cursor()
    cur.execute('SELECT type FROM zgundam')
    menu = cur.fetchall()
    menu = sorted(set(menu), key=menu.index)
    cur.close()
    get_connection().close()
    return menu

@app.route('/search')
def index():
    return render_template('index.html', len = 0, data = [])

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/')
def search():
    IsValue = False
    menu = create_pulldown_menu()
    print(menu)
    return render_template('index2.html', menu = menu, IsValue = IsValue)

@app.route('/resister')
def resister():
    return render_template('commons/resister.html', API_key = API_key)

@app.route('/search2')
def search2():
    IsValue = False
    return render_template('commons/search2.html', IsValue = IsValue)

@app.route('/post', methods=['POST'])
def post():
    IsValue = False

    budget = request.form['budget']
    type = request.form['type']
    print(budget)
    print(type)
    if not type and not budget:
        IsValue = True
        return render_template('commons/search2.html', IsValue = IsValue)

    cur = get_connection().cursor()

    if type and not budget:
        cur.execute('SELECT type,money,place,cando FROM zgundam WHERE type LIKE %s ORDER BY money ASC', (type,))
        data = cur.fetchall()
        cur.close()
        get_connection().close()
    elif budget and not type:
        cur.execute('SELECT type,money,place,cando FROM zgundam WHERE money <= %s ORDER BY money ASC', (budget,))
        data = cur.fetchall()
        cur.close()
        get_connection().close()
    else:
        cur.execute('SELECT type,money,place,cando FROM zgundam WHERE money <= %s AND type LIKE %s ORDER BY money ASC', (budget,type,))
        data = cur.fetchall()
        cur.close()
        get_connection().close()

    return render_template('index.html', budget = budget, type = type, data = data, len = len(data), placeID = "ChIJS4HJ7-PlGGARueQWOdCD_TA", API_key = API_key)

@app.route('/resister_post', methods=['POST'])
def registing():
    type = request.form['type']
    money = request.form['money']
    #placeID = request.form['placeID']
    place = request.form['place']
    cando = request.form['cando']

    if type and money and place and cando:
        print(type, money, place, cando)
        IsValue = False

        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT max(id) from zgundam;')
        id = cur.fetchone()[0]
        print(id)
        id += 1
        print(id)
        cur.execute('INSERT INTO zgundam(id, type, money, place, cando) VALUES(%s, %s, %s, %s, %s);', (id, type, money, place, cando))
        cur.close()
        conn.commit()
        conn.close()

        IsRegistration = True

        return render_template('commons/search2.html', IsValue = IsValue, IsRegistration = IsRegistration)
    else:
        IsValue = True
        return render_template('commons/resister.html', IsValue = IsValue, API_key = API_key)

if __name__ == "__main__":
    app.run()
