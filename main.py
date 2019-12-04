#using: utf-8
# 色々引っ張ってきたり、定義したり
from flask import Flask, render_template, session, redirect, url_for, escape, request
import psycopg2
import psycopg2.extras
import os
app = Flask(__name__)
# ↓はGoogle Maps APIのAPIキーを定義してます。APIキーというのは鍵です。
# API_key = os.environ.get('gmap_API')

# データベースに接続する関数です。
def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

"""
この関数はジャンルのプルダウンメニューの中身を自動で作れればいいよねって思って作ったんだけど、
データの整形がめんどくさく感じてしまったので、放置されている。

def create_pulldown_menu():
    cur = get_connection().cursor()
    cur.execute('SELECT type FROM zgundam')
    menu = cur.fetchall()
    menu = sorted(set(menu), key=menu.index)
    cur.close()
    get_connection().close()
    return menu
"""

# 最初にアクセスされるページ
@app.route('/')
def index():
    IsValue = False
    return render_template('index.html', IsValue = IsValue)

# 登録ページの表示
@app.route('/register')
def register():
    return render_template('commons/register.html')

# 検索の過程
@app.route('/searching', methods=['POST'])
def post():
    IsValue = False

    budget = request.form['budget']
    type = request.form['type']
    print(budget)
    print(type)
    if not type and not budget:
        IsValue = Truec
        return render_template('index.html', IsValue = IsValue)

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

    return render_template('commons/result.html', budget = budget, type = type, data = data, len = len(data))

# 投稿の過程
@app.route('/register_post', methods=['POST'])
def registing():
    type = request.form['type']
    money = request.form['money']
    #placeID = request.form['placeID']
    place = request.form['place']
    cando = request.form['cando']
    identity = request.form['identity']

    if type and money and place and cando and identity:
        print(type, money, place, cando, identity)
        IsValue = False

        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT max(id) from zgundam;')
        id = cur.fetchone()[0]
        print(id)
        id += 1
        print(id)
        cur.execute('INSERT INTO zgundam(id, type, money, place, cando, identity) VALUES(%s, %s, %s, %s, %s,%s);', (id, type, money, place, cando, identity))
        cur.close()
        conn.commit()
        conn.close()

        IsRegistration = True

        return render_template('index.html', IsValue = IsValue, IsRegistration = IsRegistration)
    else:
        IsValue = True
        return render_template('commons/register.html', IsValue = IsValue, API_key = API_key)

# 各URL用の概要ページ
@app.route('/result/<name>')
def hello(name):
    return render_template('commons/detail_template.html')

#ログイン
@app.route('/login', methods=['POST'])
def login():
    identity = request.form['identity']
    password = request.form['password']
    print(identity)
    print(password)

    #ucgundamから一致するか検索する
    cur = get_connection().cursor()
    cur.execute('SELECT identity,password FROM ucgundam WHERE identity LIKE %s AND password LIKE %s', (identity,),(password,))
    #cur.execute('SELECT password FROM ucgundam WHERE password  LIKE %s', (password,))
    data = cur.fetchall()
    cur.close()
    get_connection().close()


#アリの場合
    #一致したらzgumdamから過去の投稿を引っ張ってくる
    if   identity and  == :


        cur = get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM zgundam WHERE identity LIKE %s ORDER BY id ASC;', (identity))
        data = cur.fetchall()
        cur.close()
        get_connection().close()

        return render_template('commons/mypage.html', id = id, type = type, money = money, place = place, cando = cando, data = data, len = len(data))

#なしの場合
    #一致しなかった場合。zgumdamのプロセスをすっ飛ばす
    else:
        IsValue = False

        conn = get_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO ucgundam(identity, password) VALUES(%s, %s);', (identity,password))
        cur.close()
        conn.commit()
        conn.close()


        return render_template('commons/mypage.html', identity = identity, )


@app.route('/delete',methods=['POST'])
def delete():
    delete_id = request.form['delete_id']
    delete_identity = request.form['delete_identity']
    print(delete_id, delete_identity)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE  FROM zgundam WHERE id')
    cur.close()
    conn.commit()
    conn.close()

    return render_template('commons/mypage.html')


# おまじない。これがないとHerokuで動かない。
if __name__ == "__main__":
    app.debug = True
    app.run()
