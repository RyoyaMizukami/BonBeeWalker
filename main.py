#using: utf-8
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import os
app = Flask(__name__)

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

@app.route('/')
def search():
    IsValue = False
    menu = create_pulldown_menu()
    print(menu)
    return render_template('commons/registration.html', menu = menu, IsValue = IsValue)

@app.route('/result')

@app.route('/test',methods=['GET', 'POST'])
def registration():
    IsValue = False
    print("test")
    if request.method == 'POST':

        place = "" #場所についての部分がどうなるかわからなかった
        type = request.form['type']
        num = request.form['num']
        cando = request.form['cando']
        registration = request.form['registration']

        print("place",place)#上記コメント同様
        print("type:",type)
        print("num:",num)
        print("can",cando)
        #cur = get_connection().cursor()
        #cur.execute('SELECT max(id) from zgundam;')
        #row = cur.fetchone()
        ##print(row)
        #cur.close()
        #id = row[0]
        #id+=1
        #id = 301
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT max(id) from zgundam;')
        row = cur.fetchone()
        id = row[0]
        id+=1
        cur.execute('INSERT INTO zgundam(id,type,money,place,cando) VALUES(%s, %s, %s, %s, %s);',(id,type,num,place,cando))
        print(id)
        cur.close()
        conn.commit()
        conn.close()


        #with get_connection() as conn:
        #    with conn.cursor() as cur:
        #        id=300
        #        cur.execute('INSERT INTO zgundam(id,type,money,place,cando) VALUES(%s, %s, %s, %s, %s);',(id,type,num,place,cando))
        #    conn.commit()
        return render_template("commons/exit.html")

@app.route('/search2')
def search2():
    IsValue = False
    return render_template('commons/search2.html', IsValue = IsValue)

@app.route('/post', methods=['GET', 'POST'])
def post():
    IsValue = False
    print("debug_post")
    if request.method == 'POST':

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
        return render_template('index.html', budget = budget, type = type, data = data, len = len(data))

if __name__ == "__main__":
    app.debug = True
    app.run()
